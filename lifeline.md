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
	color:cornflowerblue;
}
.listing-item {color:cornflowerblue;}
.listing-item a { margin-left:1em; color:#4da6ff;}
.listing-item a:hover { color:#0590f0;}
@media all and (max-width:768px){
.listing-item{text-indent:0em;}
.listing {margin-left: -2em;}
}
@media all and (min-width:768px){
.listing-item{text-indent:5em;}
}
</style>

<ul class="listing" style="list-style-type:none;font-weight:normal;margin-top:2em;">
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator"><i class="fa fa-calendar"></i>&nbsp;&nbsp;{{ y }}</li>
  {% endif %}
  <li class="listing-item">
		<time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%B %-d " }}</time>
        <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
