# FastAPI框架的源码阅读（`0.65.1`版本）

从github上下载源码，或者`pip install fastapi`，然后在pycharm中`import fastapi`，就可以鼠标点击的方式进入源码阅读了。  
**注意**，本文档不是源码的一部分，只是为了方便，将原来的README.md改为了OriginalREADME.md。


## 源码来源
https://codeload.github.com/tiangolo/fastapi/zip/refs/tags/0.65.1

## 框架介绍
可自行去官网查看。

## 本文档作用
作为链接文件，将所有源码阅读中的点串起来。

## 使用说明
- 预备知识
  - Python基本语法
  - 网络基础知识
- 推荐使用Pycharm，版本不限，但是我目前使用的是2020.3，打开文件夹，配置好Interpreter，安装好以下包：
  - `starlette`
  - `pydantic`
  - `flip`
  - `mypy`
  - `flake8`
  - ...
- 进入`fastapi`文件夹下，然后打开`__init__.py`，可以看到最开始的注释，然后跟着注释跳转查看即可；
- ...
- 阅读体验：
  - 如果你用的是社区版，且在windows下，pycharm中默认注释是灰度的，不影响代码阅读，
  可是如果我们主要看注释，可以稍微调整一下
    - 进入Settings，然后Editor -> Color Scheme -> Language Defaults
    - 然后在打开的页面中，待选框中第四行找到Comments，双击选择第三项Line comment
    - 然后在右边Foreground旁边，点击后选择自己喜欢的颜色，最后确认。我选择蓝色，较为醒目。
  - 按住Ctrl，同时鼠标点击想跳转的函数或者类，可以直接跳转；
- 注释模板说明
  - **概览**：本文件作用；
  - **全局变量**：本文件的全局设置；
  - **外部导入**：导入模块、变量等的说明；
  - **代码格式说明**：简要有些不符合PEP8代码风格的地方；
  - **better-codes**：heavily opinionated
  - **代码逻辑**：重点，可能会分散到源码各个部分说明。

## 标记说明
- 因为源码中`#`类型的注释非常少（仅在encoders中有两行），所以，基本可以认为`#`类型的注释就是额外加的`源码阅读笔记`；
- 源码中的中文部分都是阅读源码的笔记（中文文档部分除外）；
- 其中如果有出现英文，并且标注John的部分都是我自己进一步阅读和参考的笔记。  

## 源码文档结构说明  

### 文件夹：
- .github：用于github相关的文件，相关的流程文档，提issue的模板，以及自动化的脚本等。
  有兴趣的小伙伴可以看看action中的文件。其中的`FUNDING.yml`被删除，不想引起误会； 
- docs：各个语言版本的教程文档，其中包含中文，见zh文件夹；
- docs_src：教程文档中有关代码实例的部分，实际文件在这里；
- fastapi：真正的源码所在文件夹，我的注释都将在这个文件夹下的各个文件中；
- pending_tests：测试用的脚本；
- scripts：各种脚本，含格式化代码，文档生成，发布，压缩等等，都是在linux类系统中可以直接执行的代码；
- test：用于框架测试的代码；

### 文件：
- `.flake8`：一款辅助检测`Python`代码是否规范的工具，想用可以`pip install flake8`安装使用；
- `.gitignore`：本文件内容里的文件或文件夹,是无法被版本管理工具`git`跟踪到的；
- `CONTRIBUTING.md`：如果你想给`fastapi`框架贡献代码，可以到这里看看；
- `LICENSE`：使用的是MIT许可，MIT许可在开源社区是用的非常广泛的一种，具有非常大的自由度；
- `mypy.ini`：`mypy` 在编译时向 `Python` 添加静态类型检查，使程序变得更加可维护，这里是其配置文件。
  想用可以`pip install mypy`安装使用；
- `OriginalREADME.md`：源码自带的`README.md`，项目介绍文档；
- `pyproject.toml`：包管理工具，使用`flip init`生成，自行配置。根据官方文档PEP517和PEP518，
  将来取代setup.py。这里的包指的是fastapi。
  - 使用方法：`python -m pip install .` 注意别漏掉后面的点（代表当前目录）
  - 其它：当我们安装`fastapi`时，有以下的方式：
    - `pip install fastapi`
    - `pip install fastapi[all]` 这种方法中的`all`，如果查看`pyproject.toml`文件，
      就会发现，是`all = [...]` 中的模块；
- `README.md`：此说明文件，非源码的一部分。


## 参考资料
- 官方文档： [PEP517](https://www.python.org/dev/peps/pep-0517)
- 官方文档： [PEP518](https://www.python.org/dev/peps/pep-0517) 
- 博客：学习fastapi middleware 源码调用顺序
  - https://www.cnblogs.com/shenwenlong/p/13279202.html
- 博客：FastAPI学习-Hello World
  - https://blog.csdn.net/weixin_42078760/article/details/104872557
- FastAPI官方文档
  - https://fastapi.tiangolo.com/


## PROGRESS

- 2021-5-31：建立此文档，准备源码阅读；

