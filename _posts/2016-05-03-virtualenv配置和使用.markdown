---
title: virtualenv 配置和使用
layout: post
categorie: Python
tag: [Pyhton]
---

## virtualenv 环境配置
virtualenv 环境有三种配置方法： 命令行，环境变量和配置文件.
***
### 命令行配置

用法:

``` bash
$ virtualenv [OPTIONS] DEST_DIR
```

选项:

    --version
        显示当前版本号。
    -h, --help
        显示帮助信息。
    -v, --verbose
        显示详细信息。
    -q, --quiet
        不显示详细信息。
    -p PYTHON_EXE, --python=PYTHON_EXE
        指定所用的python解析器的版本，比如
        --python=python2.5 就使用2.5版本的解析器创建新的隔离环境。
        默认使用的是当前系统安装(/usr/bin/python)的python解析器
    --clear
        清空非root用户的安装，并重头开始创建隔离环境。
    --no-site-packages
        令隔离环境不能访问系统全局的site-packages目录。
    --system-site-packages
        令隔离环境可以访问系统全局的site-packages目录。
    --unzip-setuptools
        安装时解压Setuptools或Distribute
    --relocatable
        重定位某个已存在的隔离环境。使用该选项将修正脚本并令所有.pth文件使用相当路径。
    --distribute
        使用Distribute代替Setuptools，
        也可设置环境变量VIRTUALENV_DISTRIBUTE达到同样效要。
    --extra-search-dir=SEARCH_DIRS
        用于查找setuptools/distribute/pip发布包的目录。
        可以添加任意数量的–extra-search-dir路径。
    --never-download
        禁止从网上下载任何数据。此时，如果在本地搜索发布包失败，virtualenv就会报错。
    --prompt==PROMPT
        定义隔离环境的命令行前缀。

***
### 环境变量

命令行的每个参数都以 ``VIRTUALENV_<UPPER_NAME>`` 的格式对应一个环境变量。
转换变量名过程中，除了将命令行参数大写外，还要把 (`-`) 替换为 (`_`) 。

举个例子，要自动安装Distribute取代默认的setuptools，可以这样设置环境变量:

``` bash
$ export VIRTUALENV_USE_DISTRIBUTE=true
$ python virtualenv.py ENV
```
等同于在命令行直接使用参数:
``` bash
$ python virtualenv.py --distribute ENV
```
有时要重复输入多个命令行参数，比如 `--extra-search-dir` 。
变成环境变量时，要用空格隔开多个参数值，例如:
``` bash
$ export VIRTUALENV_EXTRA_SEARCH_DIR="/path/to/dists /path/to/other/dists"
$ virtualenv ENV
```
等同于:
``` bash
$ python virtualenv.py --extra-search-dir=/path/to/dists --extra-search-dir=/path/to/other/dists ENV
```
***
### 配置文件

virtualenv还能通过标准`ini`文件进行配置。
在Unix和Mac OS X中是 ``$HOME/.virtualenv/virtualenv.ini`` ，
在Windows下是 ``%HOME%\\virtualenv\\virtualenv.ini`` 。

配置项名称就是命令行参数的名称。例如，参数 ``--distribute`` 在`ini`文件如下:
``` ini
[virtualenv]
distribute = true
```
象 ``--extra-search-dir`` 这样的多值命令行参数，在`ini`文件中要用断行将多个值隔开:
``` ini
[virtualenv]
extra-search-dir =
    /path/to/dists
    /path/to/other/dists
```
`virtualenv --help` 可以查看完整的参数列表。

## 创建虚拟环境

安装好之后，我们就可以使用`virtualenv`命令创建Python虚拟环境了。
这个命令有一个需要的参数：虚拟环境的名称。
一个指定名称的文件夹和在里面的、与虚拟环境相关的所有文件会在当前目录下被创建。
一般给虚拟环境约定命名为`venv`：
``` bash
$ virtualenv venv
New python executable in venv/bin/python2.7
Also creating executable in venv/bin/python
Installing setuptools............done.
Installing pip...............done.
```
现在你有一个`venv`文件夹和一个全新的虚拟环境，包含一个私有的Python解释器。
使用虚拟环境的时候，你必须“激活”它。
如果你是使用bash命令行工具(Linux和Mac OSX用户)，你可以使用这个命令激活虚拟环境：
``` bash
$ source venv/bin/activate

```
如果你是使用Microsoft Windows，激活命令是：
``` dos
> venv\Scripts\activate
```
当虚拟环境被激活了，Python解释器的位置会被添加到 `PATH` 中，但是这个改动并不是永久的；
它只影响当前命令会话。提醒一下，你激活了虚拟环境，该激活命令会将环境的名称包含在命令提示符里面：
``` bash
(venv)$
```
当你在虚拟环境中完成工作并想回到全局Python解释器，在命令提示符中输入 `deactivate` 就可以了。
