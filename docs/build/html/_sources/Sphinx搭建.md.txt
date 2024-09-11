# 引言

## 前言
通过利用Sphinx+GitHub+Read the Docs实现文档管理和发布。

## 要求

GitHub账户

sphinx账户

## 参考

[搭建在线电子书：Sphinx + Github + ReadTheDocs - 测试开发小记 - 博客园 (cnblogs.com)](https://www.cnblogs.com/hiyong/p/15376880.html#4-配置主题)

[无法构建项目 ·问题 #923 ·阅读文档/sphinx_rtd_theme (github.com)](https://github.com/readthedocs/sphinx_rtd_theme/issues/923)

## 定义
无。

# 创建仓库

Read the Docs导入文档有两种方式，一种是一键导入，使用下列账户可实现。另一种是通过仓库url导入。本文采取的为GitHub仓库。

> **导入不支持ssh连接**

- gitbub
- gitlab
- Bitbucket

# 本地Sphinx文档

在GitHub新建仓库并拉取到本地。

## 安装Sphinx

> **安装需要python环境**

```
pip install -U sphinx
```

## 创建文档

通过sphinx命令初始化目录

```shell
sphinx-quickstart
Welcome to the Sphinx 4.2.0 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name: 测试开发小记
> Author name(s): hiyongz
> Project release []: 0.1.0

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
#使用ch_ZH会导致乱码
> Project language [en]: en
```

本文目录结构如下

```shell
docs
    ├─build
    │  ├─doctrees
    │  └─html
    │      ├─_sources
    │      └─_static
    │          ├─css
    │          │  └─fonts
    │          └─js
    └─source
```

- docs sphinx文件目录
- build 存放编译后的文件
- source/_static 存放静态文件
- source/_templates 存放模板文件
- source/conf.py 项目配置文件，上面的配置可以在这里面修改
- source/index.rst 首页

## 编译

> 本文使用window环境

```shell
.\make html
```

## 配置主题

- 安装sphinx_rtd_theme主题

```shell
pip install sphinx_rtd_theme
```

- 配置conf.py

```python
#conf.py
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```

- 重新编译

```
.\make html
```

## 配置MakeFile

使用markdown进行文档编辑需要安装对应插件。

- 安装recommonmark插件

```
pip install recommonmark
```



- 安装支持markdown表格的插件

```
pip install sphinx_markdown_tables
```



- 配置conf.py 文件

```
extensions = ['recommonmark','sphinx_markdown_tables'] 
```

- 修改目录

```
#index.rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
    windows-shortcuts.md
```

# 上传仓库

```shell
git add .
git commit -m "sphinx"
git push
```

# 上传Read the Docs

> 配置文件中需要声明conf.py位置和需要的配置文件，这里安装库较少直接写在配置文件中，也可使用requirements.txt管理需要安装的库。

使用Read the Docs发布Sphinx文档需要配置文件，在最顶层目录创建"**.readthedocs.yaml**"文件。

## 配置文件

```
# Read the Docs configuration file for Sphinx projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the OS, Python version and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.12"
#安装库
  jobs:
    post_create_environment:
      - python -m pip install sphinx_rtd_theme
      - python -m pip install recommonmark
      - python -m pip install sphinx_markdown_tables
    # You can also specify other tool versions:
    # nodejs: "20"
    # rust: "1.70"
    # golang: "1.20"

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/source/conf.py
  # You can configure Sphinx to use a different builder, for instance use the dirhtml builder for simpler URLs
  # builder: "dirhtml"
  # Fail on all warnings to avoid broken references
  # fail_on_warning: true

# Optionally build your docs in additional formats such as PDF and ePub
# formats:
#   - pdf
#   - epub

# Optional but recommended, declare the Python requirements required
# to build your documentation
# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
# python:
#   install:
#     - requirements: docs/requirements.txt

```

## 绑定仓库

绑定GitHub账户，并选择对应GitHub库。

## 构建在线文档

使用Read the Docs的buld一键构建在线文档。构建完成后可通过对应网址访问。