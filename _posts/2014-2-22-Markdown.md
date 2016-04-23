---
layout: post
title: 标记语言 Markdown 简介
date: 2014-2-22
categories: blog
tags: [Markdown]
description: 标记语言 Markdown 简介
---

# 一、什么是 Markdown？

Markdown 是一种轻量级的 __标记语言__，相对于复杂的 [HTML](http://www.w3school.com.cn/html/index.asp) 而言，M↓ 易读易写，非常容易学习掌握。

所谓标记语言，就是标识一段文本在文档中的性质的代码。譬如上文中加粗的 `标记语言` 四个字，在 HTML 中就用 `<strong>标记语言</strong>` 来标识；又比如一级标题 `一、什么是 Markdown？` 在 HTML 中就用 `<h1>标记语言</h1>` 来标识。

从上述例子中可以看出，使用 HTML 非常繁琐。M↓ 对这些标记符号进行了简化处理，使得作者更专注于内容而不是格式，并且源文件看上去清晰明了。

可见 M↓ 来源于 HTML，但它不会取代 HTML。因为 HTML 是一种发布的格式，M↓ 是一种书写的格式。M↓ 的语法种类很少，只对应 HTML 标记的一小部分。但不在 M↓ 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。

# 二、标准 Markdown 的语法规范

Markdown 语法形式并不单一，譬如 `-` 、 `+` 与 `*` 都可以作为无序列表的标记，但本文只取其中一种形式介绍。

## 1、标题

```markdown
# 1级标题
## 2级标题
### 3级标题
```

根据 `#` 的数目可以支持 1-6 级标题。

## 2、__加粗__ 、 _斜体_ 以及 ~~删除~~

```markdown
__加粗__ 、 _斜体_ 以及 ~~删除~~
```

## 3、列表

```markdown
- Markdown 支持：
 1. 有序列表；
 2. 无序列表；
- 列表允许嵌套。
```

- Markdown 支持：
 1. 有序列表；
 2. 无序列表；
- 列表允许嵌套。

## 4、引用与转义符号 \\

```markdown
> Markdown 使用 `\` 插入一些特殊符号，如 \`
``` 

> Markdown 使用 `\` 插入一些特殊符号，如 \`

## 5、代码

    ```markdown
    区块代码有两种方式：
    1、左侧统一缩进四个空格；
    2、用```包围，并可注明语言。
    ```

段内代码由 \` 包围，如上述的「Markdown 使用 `\` 插入一些特殊符号」。

## 6、超链接、分割线与图片

```markdown
[博客地址](http://blog.zhaohengbo.com/)

---

![微信二维码](http://7xrrbc.com1.z0.glb.clouddn.com/wechat2code.jpg)
```

[博客地址](http://blog.zhaohengbo.com/)

---

![微信二维码](http://7xrrbc.com1.z0.glb.clouddn.com/wechat2code.jpg)

# 三、扩展的 Markdown 方言

随着 Markdown 的不断发展，不断有人对其语法进行扩展，产生了许多方言。其中一个比较通用的扩展是表格：

```markdown
| 项目  | 单价  | 数量 |
| :--   | :--:  | --: |
| 计算机| \$1600| 15   |
| 手机  | \$120 | 340  |
```

| 项目  | 单价  | 数量 |
| :--   | :--:  | --: |
| 计算机| \$1600| 15   |
| 手机  | \$120 | 340  |

```
除此之外，还有脚注[^footnote]、流程图、时序图、Todo列表等。由于这些
[^footnote]: 这里是脚注
```

除此之外，还有脚注[^footnote]、流程图、时序图、Todo列表等。由于这些

[^footnote]: 这里是脚注

```seq
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
```

```flow
st=>start: Start:>https://www.zybuluo.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```

- [ ] **Cmd Markdown 开发**
    - [ ] 改进 Cmd 渲染算法，使用局部渲染技术提高渲染效率
    - [ ] 支持以 PDF 格式导出文稿
    - [x] 新增Todo列表功能 [语法参考](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments)
    - [x] 改进 LaTex 功能
        - [x] 修复 LaTex 公式渲染问题
        - [x] 新增 LaTex 公式编号功能 [语法参考](http://docs.mathjax.org/en/latest/tex.html#tex-eq-numbers)
- [ ] **七月旅行准备**
    - [ ] 准备邮轮上需要携带的物品
    - [ ] 浏览日本免税店的物品
    - [x] 购买蓝宝石公主号七月一日的船票

名词 1
:   定义 1（左侧有一个可见的冒号和四个不可见的空格）

代码块 2
:   这是代码块的定义（左侧有一个可见的冒号和四个不可见的空格）

# 四、Markdown 编辑平台简介
