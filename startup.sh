#!/bin/bash

cd /src

# 更新依赖
bundle update

# 构建
jekyll build 

# 启动 web
bundle exec jekyll server host --host 0.0.0.0
