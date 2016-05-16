---
layout: page
title: "Shared"
description: "独乐乐不如众乐乐"
header-img: "img/orange.jpg"
---

## # 推荐阅读

- [How to Build a Blog？]({% post_url 2016-05-16-BulidBlog %})

- [标记语言 Markdown 简介]({% post_url 2014-02-22-Markdown %})

- [推荐：双拼输入法]({% post_url 2009-11-30-zirjma %})

## # 中学时代文集

{% for post in site.categories.articles %}

- [{{ post.title }}]({{ post.url }})

{% endfor %}

<!--
<ul class="listing" style="list-style-type: none;font-weight: bold;">
{% for post in {{site.categories.articles}} %}
  <li class="listing-item" style="text-indent:1em;font-weight:normal;">
  <a href="{{ post.url }}" title="{{ post.title }}" style="margin-left:1em;"><i class="fa fa-link">&nbsp;&nbsp;</i>{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
-->