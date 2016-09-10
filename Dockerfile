#
# Author: LM
# Date: 08/09/2016


FROM ruby
MAINTAINER LM "lm.91@qq.com"

# Set the env variable DEBIAN_FRONTEND to noninteractive
ENV DEBIAN_FRONTEND noninteractive

#移除默认源, 使用科大 debian 源, 使用淘宝 rubygem 源 
RUN sed -i 's/httpredir.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.ustc.edu.cn\/debian-security/g' /etc/apt/sources.list && \
    gem sources --add https://ruby.taobao.org/ --remove https://rubygems.org/ && \
    bundle config mirror.https://rubygems.org https://ruby.taobao.org

# Installing the 'apt-utils' package gets rid of the 
# 'debconf: delaying package configuration, since apt-utils is not installed'
# error message when installing any other package with the apt-get package manager.
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y nodejs npm ruby-dev && \
    rm -rf /var/lib/apt/lists/*

# 安装
RUN gem update && \ 
    gem install jekyll bundler jekyll-watch 

VOLUME /src

EXPOSE 4000

# Start web
CMD ["/bin/bash", "/src/startup.sh"]

