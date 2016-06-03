#!usr/bin/bash

JAVA_TAR_FILE='jdk-8u91-linux-x64.tar.gz'
JAVA_V='jdk1.8.0_91'

# 1. 解压安装 JAVA

sudo mkdir /usr/lib/jvm
sudo tar zxvf ${JAVA_TAR_FILE} -C /usr/lib/jvm
sudo mv /usr/lib/jvm/${JAVA_V} /usr/lib/jvm/java


# 2. 添加环境变量

echo 'export JAVA_HOME=/usr/lib/jvm/java' >> ~/.bashrc
echo 'export JRE_HOME=${JAVA_HOME}/jre' >> ~/.bashrc
echo 'export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib' >> ~/.bashrc
echo 'export PATH=${JAVA_HOME}/bin:$PATH' >> ~/.bashrc

# 3. 配置默认JDK版本

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java/bin/java 300
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java/bin/javac 300
sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/java/bin/jar 300
sudo update-alternatives --install /usr/bin/javah javah /usr/lib/jvm/java/bin/javah 300
sudo update-alternatives --install /usr/bin/javap javap /usr/lib/jvm/java/bin/javap 300

# 4. 配置JAVA
sudo update-alternatives --config java

# 若是初次安装 JDK， 将提示：
#　There is only one alternative in link group java (providing /usr/bin/java): /usr/lib/jvm/java/bin/java
# 无需配置。

# 5. 测试

java -version
