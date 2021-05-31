# FastAPI框架的源码阅读（0.65.1版本）

从github上下载源码，或者pip install fastapi，然后在pycharm中import fastapi，就可以鼠标点击的方式进入源码阅读了。  
注意，本文档不是源码的一部分，只是为了方便，将原来的README.md改为了OriginalREADME.md。


## 源码来源
https://codeload.github.com/tiangolo/fastapi/zip/refs/tags/0.65.1

## 框架介绍
可自行去官网查看。

## 本文档作用
作为链接文件，将所有源码阅读中的点串起来。

## 标记说明
源码中的中文部分都是阅读源码的笔记（中文文档部分除外），其中如果有出现英文，并且标注John的部分都是我自己进一步阅读和参考的笔记。  

## 源码文档结构说明  

文件夹：
- .github：用于github相关的文件，相关的流程文档，提issue的模板，以及自动化的脚本等。有兴趣的小伙伴可以看看action中的文件。  
- docs：各个语言版本的教程文档，其中包含中文，见zh文件夹；
- docs_src：教程文档中有关代码实例的部分，实际文件在这里；
- fastapi：真正的源码所在文件夹，我的注释都将在这个文件夹下的各个文件中；
- pending_tests：测试用的脚本；
- scripts：各种脚本，含格式化代码，文档生成，发布，压缩等等，都是在linux类系统中可以直接执行的代码；
- test：用于框架测试的代码；

文件：




## PROGRESS


- 2021-5-31：建立此文档，准备源码阅读；

