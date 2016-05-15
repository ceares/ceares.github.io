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

### 简单三步初具雏形

实际上，建立 GitHub 博客只需要非常简单的三个步骤就足够了：

1. 注册一个 [GitHub](https://github.com/) 账户，假设账户名为 `username`；
2. 选择一个 [现成的博客模版](http://jekyllthemes.org/)，进入模版主页找到其项目源文件，然后 fork 它。以本博客为例：
  - 本博客的项目主页：[ceares/ceares.github.io](https://github.com/ceares/ceares.github.io)
  - 点击右上角的 fork 按钮，将该项目 fork 至自己的 GitHub 仓库（Repositories）中
3. 登入自己的 GitHub 仓库，将该项目的名称更改为 `username`.github.io，同时删除项目根目录中的 CNAME 文件（如果存在）。

现在，已经可以通过 http://`username`.github.io 访问 ~~自己~~ 的博客了。在这里之所以将自己删除，显而易见，这个博客除了源文件放在自己的仓库里以外，无论其外观还是内容都还是他人的。

### 博客项目的典型结构

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
  - 1992-04-13-FirstArticle.md
- imges
  - favicon.ico
- css
- js

它们的详细用处请参阅 [Jekyll 文档](http://jekyllcn.com/docs/structure/)，这里简单介绍如下：

README.md
:   项目说明文档。属于描述性文件，与博客本身关联不大。

CNAME
:   用于绑定个人域名，并非必要的文件。

index.html
:   博客架构文档。

_config.yml
:   博客配置文档。

_includes
:   存放一些重复调用的 html 代码块，如导航栏、底栏等。

_layouts 
:   存放规定博客页面布局的文件。

About.md、404.html 等 `.md` 或 `.html` 文件 
:   非必须的，用于生成博客的一个子页面。

imges、css、js 等文件夹 
:   非必须的，通常用来存放各种资源文件。

最重要的 _posts 文件夹 
:   博文都存放在里面，如 `1992-04-13-FirstArticle.md`，支持 Markdown、html 类型。
 
博客外观细节的调整虽然并不复杂，但却非常繁琐，需要大量 Jekyll[^Jekyll] 、Markdown[^Markdown]、HTML/CSS[^HTMLCSS] 与 JavaScript[^JavaScript] 等方面的基础性知识。若有一定的编程功底可能比较迅速就能掌握，否则也不是一朝一夕就能讲明白的，在此不再赘述。

[^Jekyll]: [Jekyll：将纯文本转换为静态博客网站](http://jekyllcn.com/)

[^Markdown]: [标记语言 Markdown 简介]({% post_url 2014-2-22-Markdown %})

[^HTMLCSS]: [HTML 教程](http://www.w3school.com.cn/h.asp) 以及 [CSS 教程](http://www.w3school.com.cn/css/index.asp)

[^JavaScript]: [JavaScript 教程](http://www.w3school.com.cn/js/)

### 撰写首篇博文

博文只能采用形如 `年-月-日-标题.后缀` 的文件名，支持 Markdown、html 类型。

以文章 `1992-04-13-FirstArticle.md` 为例，其内容如下：

```
---
title: 第一篇博文
tags: [范例]
---

这里是正文，建议采用 Markdown 语法书写。
```

其中 `---` 包围的部分应参考 `_posts/` 里原有博文的规范书写。

值得注意的是，由于多方面的原因，博文书写完成后，需要等待一段时间后才能生效。

### 使用 Git 摆脱网页端的束缚

如果觉得在网页端撰写博文相当不得劲，可以先下载安装一个 [Git 工具](https://git-scm.com/)。

1. 启动 Git Bash；
2. 输入命令 `$ cd ~/.ssh`，如果提示 No such file or directory 说明是首次使用；
3. 继续输入命令 `ssh-keygen -t rsa -C "E-mail"`，其中 E-mail 可以填写 Github 注册时的邮箱地址；
4. 一路回车，直到提示 `The key's randomart image is:` 后出现文本图形。

下面将生成的 ssh key 文件添加到 GitHub 上：

1. 打开文件 `C:\Users\Administrator\.ssh\id_rsa.pub`，可能需要先设置显示隐藏文件；
2. 登陆 GitHub，点击右上角自己的头像下拉菜单中的 Settings 进入账户设置；
3. 在 Personal settings 的 SSH and GPG keys 一项中，点击 New SSH key 按钮添加 SSH keys；
4. 将步骤 1 打开文件中的全部内容准确复制到 key文本框里面。

完成上述步骤后，可以在 Git Bash 中输入命令 `ssh -T git@github.com` 测试是否成功，如果反馈 

```bat
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

则说明已经成功。

#### pull & push

`git pull` 和 `git push`[^push] 命令可以实现本地与云端同步，在使用它们之前，需要先将博客项目 clone 到本地。即在本地存储位置执行 cmd 命令：

```bat
git clone https://github.com/username/username.github.io.git
```

为了方便，可以在当前路径保存两个批处理文件：

- pull.bat：将 GitHub 端的数据提取到本地

```bat
cd username.github.io
git pull
```

- push.bat：将本地的数据推送到 GitHub 

```bat
cd username.github.io
git add .
git commit -a -m "msg"
git push origin master
```

[^push]: [git push 提示 Everything up-to-date，但 GitHub 未更新]({% post_url 2016-04-23-gitpush %})

在 `../username.github.io/_posts/` 路径下撰写博文，再运行 `push.bat` 就能将改动更新至 GitHub。

#### 与 Droid Edit 同步

Droid Edit 是一款手机文本编辑软件，内置一个小型的 Git 环境，可以通过该软件在手机端撰写博文。

### 个性化的域名

`username`.github.io 的域名缺乏个性，也不便于推广。

三百M 内联和外链

### 进一步地探索


