# pygong

一种用于python的程序开发的简单公共库。

用法
确保wheel是最新版本：python3 -m pip install --user --upgrade setuptools wheel

检查setup.py是否有错误
python setup.py check
打包一个源代码包：python setup.py sdist build
打包一个wheels格式的包：
（1）python setup.py bdist_wheel --universal
（2）python3 setup.py sdist bdist_wheel