---
title: 用 add-apt-repository 管理 apt-get 源
layout: post
categories: Ubuntu
tag: [Ubuntu,Liunx,apt-get]
---

# 安装
```bash
$ sudo apt-get install python-software-properties
```

# 更新
```bash
sudo apt-get update
```

# 使用
```bash
sudo add-apt-repository "deb http://archive.canonical.com/ubuntu maverick partner"
```

# 帮助

··· bash
add-apt-repository --help
Usage: add-apt-repository \<sourceline\>

* `add-apt-repository` is a script for adding apt `sources.list` entries.
It can be used to add any repository and also provides a shorthand
syntax for adding a Launchpad `PPA` (Personal Package Archive)
repository.

* <sourceline> - The apt repository source line to add. This is one of:
  - a complete apt line in quotes,
  - a repo url and areas in quotes (areas defaults to 'main')
  - a PPA shortcut.
  - a distro component

  - Examples:
    - apt-add-repository 'deb http://myserver/path/to/repo stable myrepo'
    - apt-add-repository 'http://myserver/path/to/repo myrepo'
    - apt-add-repository 'https://packages.medibuntu.org free non-free'
    - apt-add-repository http://extras.ubuntu.com/ubuntu
    - apt-add-repository ppa:user/repository
    - apt-add-repository multiverse

If `--remove` is given the tool will remove the given sourceline from your
`sources.list`


* Options:
  - **-h**, --help            show this help message and exit
  - **-m**, --massive-debug   将多个调试信息输出到命令行
  - **-r**, --remove          从 `sources.list.d` 目录移除仓库
  - **-k** KEYSERVER, --keyserver=KEYSERVER 密钥服务器 URL。
  默认：`hkp://keyserver.ubuntu.com:80/`
  - **-s**, --enable-source   允许从仓库下载源码包
  - **-y**, --yes             对所有问题都设定回答为是
···
  
  
# 老办法

··· bash
cp /etc/apt/sources.list /etc/apt/sources.list.bak
vim /etc/apt/sources.list
···

添加以下的源：

··· bash
# 中科大：
deb http://mirrors.ustc.edu.cn/ubuntu/ precise-updates main restricted
deb-src http://mirrors.ustc.edu.cn/ubuntu/ precise-updates main restricted
deb http://mirrors.ustc.edu.cn/ubuntu/ precise universe
deb-src http://mirrors.ustc.edu.cn/ubuntu/ precise universe
deb http://mirrors.ustc.edu.cn/ubuntu/ precise-updates universe
deb-src http://mirrors.ustc.edu.cn/ubuntu/ precise-updates universe
deb http://mirrors.ustc.edu.cn/ubuntu/ precise multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ precise multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ precise-updates multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ precise-updates multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ precise-backports main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ precise-backports main restricted universe multiverse

deb http://security.ubuntu.com/ubuntu precise-security main restricted
deb-src http://security.ubuntu.com/ubuntu precise-security main restricted
deb http://security.ubuntu.com/ubuntu precise-security universe
deb-src http://security.ubuntu.com/ubuntu precise-security universe
deb http://security.ubuntu.com/ubuntu precise-security multiverse
deb-src http://security.ubuntu.com/ubuntu precise-security multiverse


# 搜狐：
deb http://mirrors.sohu.com/ubuntu/ precise-updates main restricted
deb-src http://mirrors.sohu.com/ubuntu/ precise-updates main restricted
deb http://mirrors.sohu.com/ubuntu/ precise universe
deb-src http://mirrors.sohu.com/ubuntu/ precise universe
deb http://mirrors.sohu.com/ubuntu/ precise-updates universe
deb-src http://mirrors.sohu.com/ubuntu/ precise-updates universe
deb http://mirrors.sohu.com/ubuntu/ precise multiverse
deb-src http://mirrors.sohu.com/ubuntu/ precise multiverse
deb http://mirrors.sohu.com/ubuntu/ precise-updates multiverse
deb-src http://mirrors.sohu.com/ubuntu/ precise-updates multiverse
deb http://mirrors.sohu.com/ubuntu/ precise-backports main restricted universe multiverse
deb-src http://mirrors.sohu.com/ubuntu/ precise-backports main restricted universe multiverse

# 网易：

deb http://mirrors.163.com/ubuntu/ precise-updates main restricted
deb-src http://mirrors.163.com/ubuntu/ precise-updates main restricted
deb http://mirrors.163.com/ubuntu/ precise universe
deb-src http://mirrors.163.com/ubuntu/ precise universe
deb http://mirrors.163.com/ubuntu/ precise-updates universe
deb-src http://mirrors.163.com/ubuntu/ precise-updates universe
deb http://mirrors.163.com/ubuntu/ precise multiverse
deb-src http://mirrors.163.com/ubuntu/ precise multiverse
deb http://mirrors.163.com/ubuntu/ precise-updates multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-updates multiverse
deb http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
```

更新：

``` bash
sudo apt-get update
sudo apt-get upgrade
```
