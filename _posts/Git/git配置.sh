#!usr/bin/bash
# 个人信息设置
# git config --global user.name='LM'
# git config --global user.email='lm.91@qq.com'

# 常用别名

git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# 其他

git config --global alias.last 'log -1 HEAD'

# 设定编辑器

echo 'export GIT_EDITOR=vim' >> ~/.bashrc
