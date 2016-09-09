# 安装
1. 更新安装源列表
``` bash
$sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
2. 设定密钥
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116
```
3. 安装
```bash
sudo apt-get update
```
  Do not install these packages if you are using 14.04, it will destroy your X server:

  sudo apt-get install xserver-xorg-dev-lts-utopic mesa-common-dev-lts-utopic libxatracker-dev-lts-utopic libopenvg1-mesa-dev-lts-utopic libgles2-mesa-dev-lts-utopic libgles1-mesa-dev-lts-utopic libgl1-mesa-dev-lts-utopic libgbm-dev-lts-utopic libegl1-mesa-dev-lts-utopic

  Alternatively, try installing just this to fix dependency issues:

  sudo apt-get install libgl1-mesa-dev-lts-utopic

  There are many different libraries and tools in ROS. We provided four default configurations to get you started. You can also install ROS packages individually.

  Desktop-Full Install: (Recommended) : ROS, rqt, rviz, robot-generic libraries, 2D/3D simulators, navigation and 2D/3D perception

  Indigo uses Gazebo 2 which is the default version of Gazebo on Trusty and is recommended.

4. 安装私人包：
```bash
sudo apt-get install ros-indigo-PACKAGE
```
e.g. 比如：
```bash
sudo apt-get install ros-indigo-slam-gmapping
```
寻找可用的包：
```bash
apt-cache search ros-indigo
```

# 初始化
在使用ROS前应该初始化 `rosdep`
```bash
sudo rosdep init
rosdep update
```
# 环境设定
* 一劳永逸的方法
```bash
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
* 为当前的shell切换环境：
```bash
source /opt/ros/indigo/setup.bash # indigo 是版本名
```

# 获得安装工具 rosintall
```bash
sudo apt-get install python-rosinstall
```
# 管理环境
***
ROS包的查找建立在变量 `ROS_ROOT` 和 `ROS_PACKAGE_PATH` 上，可以命令查看：
```bash
$ printenv | grep ROS
```
启动ROS
```bash
$ source /opt/ros/<distro>/setup.bash
```
e.g. 比如：
```bash
$ source /opt/ros/indigo/setup.bash
```
# 建立一个ROS Workspace

建立一个 `catkin workspace`
```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
```
即使工作空间是空的，仅仅包含 `CMakeLists.txt` 链接，仍然可以构建：
```bash
$ cd ~/catkin_ws/
$ catkin_make
```
`catkin_make` 命令在`catkin workspaces`中是一个方便的命令，运行后旗下产生两个文件夹：
* 'build'
* 'devel' 有几个setup.*sh文件

在运行新的setup.sh文件时先运行：
```bash
$ source devel/setup.bash
```
并保证 `ROS_PACKAGE_PATH` 环境变量中包含你所在的目录。
```bash
$ echo $ROS_PACKAGE_PATH
/home/youruser/catkin_ws/src:/opt/ros/indigo/share:/opt/ros/indigo/stacks
```
