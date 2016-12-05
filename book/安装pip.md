在[安装mysql](https://github.com/TanLian/tlforum/blob/master/book/%E5%AE%89%E8%A3%85mysql.md)一文中我们已经安装了setuptools，安装了这个后就会有一个工具easy_install
可以直接`easy_install pip`来安装pip，不过我试了一下，安装得超级慢，不推荐用这种方法。我们编译安装pip（安装包在tools目录里面有）。  
`cd pip-9.0.1`  
`python setup.py build`  
`python setup.py install`  

配置pip源为豆瓣的源，可以大幅加快`pip install`的速度。  
`mkdir ~/.pip`  
`vim ~/.pip/pip.conf`  
将下列内容写入pip.conf，然后保存退出即可。  
`[global]`  
`index-url = http://pypi.douban.com/simple`  
`trusted-host = pypi.douban.com`  
`disable-pip-version-check = true`  
`timeout = 120`  

