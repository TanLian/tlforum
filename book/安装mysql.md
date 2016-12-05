* 安装mysql  
`yum install -y mysql-server mysql mysql-devel`  
* 设置mysql开机自启动  
`chkconfig mysqld on`
* 启动mysql数据库
`/etc/init.d/mysql start`或者`service mysqld start`
* 修改root账号默认密码
`mysqladmin -u root password '123456'`  
我将root的默认密码设置成了123456，当然也可以设成其他值。

* 安装MySQLdb  
先安装必要的库
`yum install -y python-devel mysql-devel zlib-devel openssl-devel`  
**安装了这些库可能还要重新编译一下python2.7**  
下载MySQL-python-1.2.5.zip（tools目录有）。  
解压该压缩包
`unzip MySQL-python-1.2.5.zip`
编译安装
`cd MySQL-python-1.2.5`  
`python setup.py build`  
`python setup.py install`  
在build那一步可能会报如下错误：
![](http://ohm24hviv.bkt.clouddn.com/no-setuptools.png)  
很明显，原因是未安装setuptools，我们安装就是了。
下载setuptools.tar.gz（tools目录有）。  
解压该压缩包.  
`tar zxf setuptools-30.0.0.tar.gz`  
安装setuptools  
`cd setuptools-30.0.0`  
`python setup.py build`
`python setup.py install`
这样setuptools就安装成功了。
再进入到MySQL-python-1.2.5目录，重新执行build、install等操作。
以下就表示安装成功:
![](http://ohm24hviv.bkt.clouddn.com/install-mysqldb-success.png)

