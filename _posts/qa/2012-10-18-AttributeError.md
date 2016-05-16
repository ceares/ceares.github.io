---
layout: post
title: AttributeError：'module' object has no attribute 
date: 2012-10-18
categories: qa
tags: [Python,QA,error]
description: Attribute Error
---

一般新学一门语言我都习惯用test或者想要实现的功能命名源码文件。

在Python中有专门的模块csv来处理该类型文件，在初次学习使用该模块时，我将源码文件命名为csv.py。

csv模块中有一个reader方法用于读取csv文件。按照示例程序编写代码，运行后一直报错：

> AttributeError: 'module' object has no attribute 'reader'

查找出错原因很久，才明白原来是源码文件命名的问题。直接命名为csv.py编译之后会有个module叫csv，因此源代码中导入的csv模块并不是我们期望的那个。

用Python、LaTeX这类语言时，如果当前路径下存在同名文件，会优先导入。因此，源码文件命名需要注意，不要与需要导入的文件冲突。
