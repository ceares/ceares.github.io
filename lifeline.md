---
layout: page
title: "Lifeline"
description: "生命在这里留下了痕迹"
header-img: "img/zhihu.jpg"
nav-display: true
---

<style type="text/css">
.listing-seperator {
	margin:1em auto;
	color:#0590f0
}
.listing-item { text-indent:3em; color:#0590f0}
.listing-item a { margin-left:0.5em; color: #0590f0}
.listing-item a:hover { text-decoration: underline}
</style>

<ul class="listing" style="list-style-type:none;font-weight:normal;margin-top:2em;">
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator"><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;{{ y }}</li>
  {% endif %}
  <li class="listing-item">
    <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%m/%d" }}</time>
    <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
