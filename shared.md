---
layout: page
title: "Shared"
description: "独乐乐不如众乐乐"
header-img: "img/shared.jpg"
custom_css_shared: true
nav-display: true
---

{% if page.custom_css_shared %}
<style type="text/css">
#school-art li {padding:0.5em 0}
@media all and (max-width:768px){
#school-art   {
-moz-column-count:1; /* Firefox */
-webkit-column-count:1; /* Safari and Chrome */
column-count:1;
margin-left:-2em}
}
@media all and (min-width:768px){
#school-art  {
-moz-column-count:2; /* Firefox */
-webkit-column-count:2; /* Safari and Chrome */
column-count:2;}
}
/*.listing-item{text-indent:1em;font-weight:normal;}*/
 </style>  
{% endif %}
  
### # 推荐阅读

- &nbsp;&nbsp;[How to Build a Jakyll Blog  on GitHub ？]({% post_url 2016-03-16-BulidBlog %})

- &nbsp;&nbsp;[标记语言 Markdown 简明语法]({% post_url 2014-02-22-Markdown %})

- &nbsp;&nbsp;[双拼自然码输入方案简介]({% post_url 2009-11-30-zirjma %})

### # 文学作品

<ul id="school-art" style="list-style-type: none;margin-top:1em">
{% for post in site.categories.articles %}
<li><a href="{{ post.url }}" >&nbsp;&nbsp;{{ post.title }}</a></li>
{% endfor %}
</ul>

<!--
<ul class="listing" style="list-style-type: none;font-weight: bold;">
{% for post in {{site.categories.articles}} %}
  <li class="listing-item" style="font-weight:normal;">
  <a href="{{ post.url }}" title="{{ post.title }}" style="margin-left:1em;"><i class="fa fa-link">&nbsp;&nbsp;</i>{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
-->