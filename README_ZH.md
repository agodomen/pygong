# pygong

一种用于python的程序开发的简单公共库。

# 用法

## 编译安装

确保wheel是最新版本：python3 -m pip install --user --upgrade setuptools wheel

检查setup.py是否有错误

方法一、

python install.py check
打包一个源代码包：python install.py sdist build
打包一个wheels格式的包：

（1）python setup.py bdist_wheel --universal

（2）python3 setup.py sdist bdist_wheel

方法二、
```shell
python -m build
pip install xxx.whl
```

## 直接安装

```shell
pip install pygong
```

# 参考资料

https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://daobook.github.io/flit/pyproject_toml.html
https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
