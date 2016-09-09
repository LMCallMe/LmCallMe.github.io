#
# Author: LM
# Date: 08/09/2016


FROM ruby
MAINTAINER LM "lm.91@qq.com"
# Set the env variable DEBIAN_FRONTEND to noninteractive
#ENV DEBIAN_FRONTEND noninteractive

#移除默认源, 添加科大源
COPY  mirrors/debian/sources.list /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y nodejs npm ruby-dev
    
# Set the env variable DEBIAN_FRONTEND to noninteractive
ENV DEBIAN_FRONTEND noninteractive

#移除默认源, 添加科大源
RUN gem sources --remove https://rubygems.org/  && \
    gem sources -a https://mirrors.ustc.edu.cn/rubygems/  
    
# 更新源
RUN gem update


# 安装
RUN gem install jekyll bundler jekyll-watch && \
    bundle config mirror.https://rubygems.org https://ruby.taobao.org

VOLUME /src

EXPOSE 4000

# Start web
CMD ["/bin/bash", "/src/startup.sh"]

