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
  - 本博客的项目主页：<https://github.com/ceares/ceares.github.io>
  - 点击右上角的 fork 按钮，将该项目 fork 至自己的 GitHub 仓库（repositories）中
3. 登入自己的 GitHub 仓库，将该项目的名称更改为 `username`.github.io；并删除项目根目录中的 CNAME 文件（如果存在）。

现在，已经可以通过 http://`username`.github.io 访问“自己”的博客了。在这里之所以将“自己”加引号，显而易见，这个博客除了源文件放在自己的仓库里以外，无论其外观还是内容都还是他人的。

## 博客项目的典型结构

[Jekyll](http://jekyllcn.com/) 博客目录的典型树形结构如下：

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

其中，

博客细节的微调虽然并不复杂，但是非常繁琐，需要大量 Markdown、HTML/CSS、JavaScript 与 Jekyll 等方面的基础性知识。若有一定的编程功底可能比较迅速就能掌握，否则也不是一朝一夕就能讲明白的，在此不再赘述。

## 撰写首篇博文

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






![]({{ site.url }}/pics/pandaman.jpg)


