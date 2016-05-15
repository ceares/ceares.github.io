---
layout: page
title: "Shared"
description: "独乐乐不如众乐乐"
header-img: "img/orange.jpg"
---

<style>a{color:#2b4180}</style>

# How to Build a Blog？

在了解如何用 GitHub Pages 搭建独立博客之前，首先应该先问自己为什么要这样做？

1. 独立博客更为个性，但也更加折腾，需要学习和钻研精神；
2. 独乐乐不如众乐乐，博客应当用来分享学习札记、心路历程等；
3. 选择更 geek 的方式也意味着收获的乐趣更多，一切付出都是值得的。

本文尽量以简明易懂的方法叙述，足以引导初学者入门，但若想追求更加完美的作品，就只能用屈原的话勉励自我了：

> 路漫漫其修远兮，吾将上下而求索！

## 简单三步初具雏形

实际上，建立 GitHub 博客只需要非常简单的三个步骤就足够了：

1. 注册一个 [GitHub](https://github.com/) 账户，假设账户名为 `username`；
2. 选择一个 [现成的博客模版](http://jekyllthemes.org/)，进入模版主页找到其项目源文件，然后 fork 它。以本博客为例：
  - 本博客的项目主页：[ceares/ceares.github.io](https://github.com/ceares/ceares.github.io)
  - 点击右上角的 fork 按钮，将该项目 fork 至自己的 GitHub 仓库（Repositories）中
3. 登入自己的 GitHub 仓库，将该项目的名称更改为 `username`.github.io；并删除项目根目录中的 CNAME 文件（如果存在）。

现在，已经可以通过 http://`username`.github.io 访问“自己”的博客了。在这里之所以将“自己”加引号，显而易见，这个博客除了源文件放在自己的仓库里以外，无论其外观还是内容都还是他人的。

## 博客项目的典型结构

Jekyll 博客目录的典型树形结构图如下：

- README.md
- CNAME
- index.html
- About.md
- 404.html
- feed.xml
- _config.yml
- _includes
  - head.html
  - foot.html
- _layouts
  - default.html
  - post.html
- _posts
  - 2016-05-15-FirstArticle.md
- imges
  - favicon.ico
- css
- js

它们的详细用处请参阅 [Jekyll 文档](http://jekyllcn.com/docs/structure/)，这里简单介绍如下：

`README.md` 
:   项目说明文档。属于描述性文件，与博客本身关联不大。
`CNAME` 
:   用于绑定个人域名，并非必要的文件。
`index.html` 
:   博客架构文档。
`_config.yml` 
:   博客配置文档。
`_includes` 
:   存放一些重复调用的 html 代码块，如导航栏、底栏等。
`- _layouts` 
:   存放规定博客页面布局的文件。
`About.md`、`404.html` 等 `.md` 或 `.html` 文件 
:   非必须的，用于生成博客的一个子页面。
`imges`、`css`、`js` 等文件夹 
:   非必须的，通常用来存放各种资源文件。
`_posts/` 文件夹 
:   最重要的文件夹，博文都存放在里面，如 `2016-05-15-FirstArticle.md`，支持 Markdown、html 类型。
 
博客外观细节的调整虽然并不复杂，但却非常繁琐，需要大量 Markdown[^Markdown]、HTML/CSS[^HTML/CSS]、JavaScript[^JavaScript] 与 Jekyll[^Jekyll] 等方面的基础性知识。若有一定的编程功底可能比较迅速就能掌握，否则也不是一朝一夕就能讲明白的，在此不再赘述。

[^Markdown]: Markdown

[^HTML/CSS]: HTML/CSS

[^JavaScript]: JavaScript

[^Jekyll] : Jekyll

## 撰写首篇博文

博文的文件名只能采用形如 `2016-05-15-FirstArticle.md` 的格式，支持 Markdown、html 类型。

博文存放在 `_posts/` 文件夹里面，其文件名只能采用形如 `2016-05-15-FirstArticle.md` 的格式，并且只支持 Markdown、html 以及 Textile 三种类型。

建议采用 Markdown 语法书写博客，其语法介绍参见「 [标记语言 Markdown 简介](http://blog.zhaohengbo.com/blog/2014/02/22/Markdown/) 」。示范如下：

```
---
layout: post
title: 第一篇博文
date: 2016-05-15
categories: blog
tags: [blog,示例]
description: 这是第一篇博文。
---

# 博文范例

这里是正文。
```

其中，`---` 包围的头信息应参考 `_posts/` 文件夹里原有博文的规范书写。

值得注意的是，由于多方面的原因，博文书写完成后，需要等待一段时间后才能生效。

定制专属内容


更改博客的细节样式需要 HTML/CSS、JavaScript 等知识，[W3School](http://www.w3school.com.cn/h.asp)
![picture](http://7xrrbc.com1.z0.glb.clouddn.com/figure_name) 上有非常详尽的教程。


## 更加地便利化

三百M 内联和外链

在网页端撰写博文相当不得劲，而且 `username`.github.io 的域名也缺乏个性，不便于推广。接下来将介绍如何弥补这些不足。

### 与电脑端和手机端同步

### 个性化的域名


定义型列表
:   除此之外，还有脚注[^footnote]、流程图、时序图、Todo列表等多种扩展语法，但它们都跟 Markdown 具体的编辑平台相关，因此不作具体介绍。

[^footnote]: 这里是脚注



![]({{ site.url }}/pics/pandaman.jpg)


