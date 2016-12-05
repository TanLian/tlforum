* 编译安装Python 2.7
Centos6.7上默认安装的是Python 2.6，而我们开发需要的是Python 2.7。  
	* 先安装gcc编译器  
`yum install -y gcc gcc-c++`
	* 解压Python-2.7.10.tgz（需要先下载，tools目录有）
`tar zxf Python-2.7.10.tgz`  
解压后会得到一个Python-2.7.10目录，如下图所示：
![](http://ohm24hviv.bkt.clouddn.com/Python-2.7.10-uncompress.png)  
	* 编译、安装  
`cd Python-2.7.10`  
`./configure`  
`make`  
`make install`  
此时python2.7应该已经编译出来了，文件完整路径为`/usr/local/bin/python2.7`
	* 修改系统默认Python为Python2.7
`mv /usr/bin/python  /usr/bin/python.bak`  
`ln -s /usr/local/bin/python2.7 /usr/bin/python`  
此时执行python命令，应该执行的就是python2.7.10了，如下图所示：
![](http://ohm24hviv.bkt.clouddn.com/Python2.7.10.png)  
	* 修正yum源
`vi /usr/bin/yum`
将第一行修改为#!/usr/bin/python2.6  
至此，Python2.7安装完毕

