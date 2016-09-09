#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lm.91@qq.com on 2016/9/8

__author__ = 'lm.91@qq.com'


import os
import sys
import json
import logging

# 将日志同时输出到文件和屏幕
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='blog.log',
                filemode='a')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

from docker import Client
cli = Client()

def exists_image(name):
    images = cli.images(all=True)
    for image in images:
        if name+":latest" in image["RepoTags"]:
            logging.info("exists image %s" % name)
            return True
    logging.info("not exists image %s" % name)
    return False

def exists_container(name):
    containers = cli.containers(all=True)
    for container in containers:
        if '/' + name in container["Names"]:
            logging.info("exists container %s" % name)
            return True
    logging.info("not exists container %s" % name)
    return False

def remove_dangling_image():
    logging.info("removing dangling images")
    for image in cli.images(filters={"dangling":True}):
        try:
            cli.remove_image(image['Id'])
        finally:
            pass
    logging.info("removed dangling images")

def build_image(name):
    logging.info("building docker image %s" % name)
    path = os.path.abspath(os.curdir)
    tag = name
    rm = True  # 去除中间容器
    generator = cli.build(path=path, rm=rm, tag=tag)
    for line in generator:
        line = line.decode()
        try:
            stream_line = json.loads(line)
            line = stream_line["stream"]
        finally:
            logging.info(line)
    remove_dangling_image()

def create_container(name,image):
    logging.info("creating container %s use image %s" % (name, image))
    path = os.path.abspath(os.curdir)
    container_id = cli.create_container(
        name=name,
        image=image,
        detach=False,  # 后台运行
        ports=[(4000, 'tcp'), (22, 'tcp')],  # 容器开放的端口
        volumes=['/src'],  # 容器的卷路径
        host_config=cli.create_host_config(
            binds={
                path: {  # 绑定到当前路径
                    'bind': '/src',
                    'mode': 'rw',
                }
            },
        port_bindings={
            4000: ('127.0.0.1', 4000),  # 将容器的 80 端口绑定到主机的 8080 端口
            22: ('127.0.0.1', 22)
         })
    )
    logging.info("created container %s use image %s" % (name, image))
    return container_id # 返回容器的ID

def stop_container(name):
    logging.info("stopping container %s" % name)
    cli.stop(name)
    logging.info("stopped container %s" % name)

def container_is_running(name):
    containers = cli.containers()
    for container in containers:
        if '/' + name in container["Names"]:
            logging.info("container %s is running" % name)
            return True
    logging.info("container %s is not running" % name)
    return False

def start_container(name):
    logging.info("starting container %s" % name)
    cli.start(name)
    logging.info("started container %s" % name)

def remove_container(name):
    logging.info("removing container %s" % name)
    cli.remove_container(name)
    logging.info("removed container %s" % name)

def force_removed_container(name):
    if container_is_running(name):
        stop_container(name)
    remove_container(name)

def yesOrNo(yes_func=None, no_func=None):
    while True:
        opt = input()
        opt = opt.lower()
        if opt in ['y', 'yes']:
            return True if yes_func is None else yes_func()
        elif opt in ['n', 'no']:
            return False if no_func is None else no_func()
        else:
            print("Use [y/n] or [yes/no]")

def build(imageName):
    if not exists_image(imageName):
        build_image(imageName)
    else:
        logging.warning(" Already have the image %s, Do you want to build again ? [y/o]" % imageName)
        if yesOrNo(no_func=sys.exit):
            build_image(imageName)

def create(containerName, imageName):
    if not exists_image(imageName):
         logging.error("You must be build the image %s before create container" % imageName)
    if not exists_container(containerName):
        create_container(containerName,imageName)
    else:
        logging.warning(" Already have the container %s, Do you want to remove it and create again ? [y/o]" % containerName )
        if yesOrNo(no_func=sys.exit):
            force_removed_container(containerName)
            create_container(containerName,imageName)

def start(containerName):
    if not exists_container(containerName):
        logging.error("You must be create the container %s before start it" % containerName)
    start_container(containerName)

if __name__ == '__main__':

    imageName = "lmcallme/gitblog"
    containerName = "gitblog"

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--build',action="store_true",
                        help='build docker image: %s' % imageName)
    parser.add_argument('-c', '--create',action="store_true",
                        help='default run docker container: %s' % containerName)

    args = parser.parse_args()

    if args.build:
        build(imageName)
    elif args.create:
        create(containerName,imageName)
    else:
        start(containerName)
