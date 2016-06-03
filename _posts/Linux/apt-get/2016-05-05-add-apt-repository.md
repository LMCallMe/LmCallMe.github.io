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

# help

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
