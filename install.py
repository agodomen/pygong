import codecs
import os
import sys

from distutils.util import convert_path
from fnmatch import fnmatchcase
from setuptools import setup, find_packages

def find_version():
    # --- get version ---
    base_version = "unknown"
    with open("src/pygong/version.py") as f:
        line = f.read().strip().split('\n')[0]
        base_version = line.replace("version = ", "").replace('"', '')
    # --- get version ---
    return base_version
import io
from os import path
# Get the long description from the README file
def find_long_description():
    long_description=None
    with io.open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


# Provided as an attribute, so you can append to these instead
# of replicating them:
standard_exclude = ["*.py", "*.pyc", "*$py.class", "*~", ".*", "*.bak"]
standard_exclude_directories = [
    ".*", "CVS", "_darcs", "./build", "./dist", "EGG-INFO", "*.egg-info"
]


# (c) 2005 Ian Bicking and contributors; written for Paste (http://pythonpaste.org)
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
# Note: you may want to copy this into your setup.py file verbatim, as
# you can't import this from another package, when you don't know if
# that package is installed yet.
def find_package_data(
        where=".",
        package="",
        exclude=standard_exclude,
        exclude_directories=standard_exclude_directories,
        only_in_packages=True,
        show_ignored=False):
    """
    Return a dictionary suitable for use in ``package_data``
    in a distutils ``setup.py`` file.

    The dictionary looks like::

        {"package": [files]}

    Where ``files`` is a list of all the files in that package that
    don"t match anything in ``exclude``.

    If ``only_in_packages`` is true, then top-level directories that
    are not packages won"t be included (but directories under packages
    will).

    Directories matching any pattern in ``exclude_directories`` will
    be ignored; by default directories with leading ``.``, ``CVS``,
    and ``_darcs`` will be ignored.

    If ``show_ignored`` is true, then all the files that aren"t
    included in package data are shown on stderr (for debugging
    purposes).

    Note patterns use wildcards, or can be exact paths (including
    leading ``./``), and all searching is case-insensitive.
    """
    out = {}
    stack = [(convert_path(where), "", package, only_in_packages)]
    while stack:
        where, prefix, package, only_in_packages = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                            or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print("Directory %s ignored by pattern %s" % (fn, pattern), file=sys.stderr)
                            # print >> sys.stderr, ( "Directory %s ignored by pattern %s" % (fn, pattern))
                        break
                if bad_name:
                    continue
                if (os.path.isfile(os.path.join(fn, "__init__.py"))
                        and not prefix):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + "." + name
                    stack.append((fn, "", new_package, False))
                else:
                    stack.append((fn, prefix + name + "/", package, only_in_packages))
            elif package or not only_in_packages:
                # is a file
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                            or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print("File %s ignored by pattern %s" % (fn, pattern), file=sys.stderr)
                            # print >> sys.stderr, (
                            #         "File %s ignored by pattern %s"
                            #         % (fn, pattern))
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out


PACKAGE = "src"
NAME = "pygong"
DESCRIPTION = "Supported for python dev common utils collection library."
AUTHOR = "gongwendong"
AUTHOR_EMAIL = "gwd163nom@163.com"
URL = "https://github.com/agodomen/pygong"
VERSION = find_version()
# __import__(PACKAGE).__version__

# name：项目的名称，name是包的分发名称。
# version：项目的版本。需要注意的是，PyPI上只允许一个版本存在，如果后续代码有了任何更改，再次上传需要增加版本号
# author和author_email：项目作者的名字和邮件, 用于识别包的作者。
# project_urls 显示的任意数量的链接。通常是文档、问题跟踪器等。
# description：项目的简短描述
# long_description：项目的详细描述，会显示在PyPI的项目描述页面。必须是rst(reStructuredText) 格式的
# packages：指定最终发布的包中要包含的packages。
# package_dir是一个字典，src目录被指定为根包。
# install_requires：项目依赖哪些库，这些库会在pip install的时候自动安装
# classifiers：其他信息，一般包括项目支持的Python版本，License，支持的操作系统。
# python_requires给出项目支持的 Python 版本。还有有个配置文件setup.cfg，相对于setup.py,此文件配置是静态元数据，内容基本不变；推荐使用setup.py配置； 具体可参考pypi官网解释;
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache",
    url=URL,
    platforms=['any'],
    keywords='python utils,python common',
    packages=find_packages(exclude=["tests.*","tests",'docs']),
    # package_data=find_package_data(PACKAGE, only_in_packages=False),
    classifiers=[
        "Development Status :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
    python_requires=">=3.2",
)
