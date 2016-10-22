---
layout: post
category : 技术 
tagline: "proxychains"
tags : [gfw, proxy]
---

## 安装

``` bash
$ sudo apt-get install proxychains
```

## 配置

``` bash
$ vim /etc/proxychains.conf
```

推荐配置

``` ini
strict_chain
proxy_dns
remote_dns_subnet 224
tcp_read_time_out 15000
tcp_connect_time_out 8000
localnet 127.0.0.0/255.0.0.0
quiet_mode

[ProxyList]
socks5 127.0.0.1 1080
```

## 使用

``` bash
$ proxychains curl https://www.twitter.com
$ proxychains git push origin master
$ proxychains dropbox start -i
```

