---
layout: page
title: "Shared"
description: "独乐乐不如众乐乐"
header-img: "img/orange.jpg"
custom_css_shared: true
nav-display: true
---

{% if page.custom_css_shared %}
<style type="text/css">
@media all and (max-width:768px){
#school-art li {
-moz-column-count:2; /* Firefox */
-webkit-column-count:2; /* Safari and Chrome */
column-count:2;}
}
@media all and (min-width:768px){
#school-art li {
-moz-column-count:3; /* Firefox */
-webkit-column-count:3; /* Safari and Chrome */
column-count:3;}
}
</style>  
{% endif %}
  
### # 推荐阅读

- &nbsp;&nbsp;[How to Build a GitHub Blog？]({% post_url 2016-05-16-BulidBlog %})

- &nbsp;&nbsp;[标记语言 Markdown 简明语法]({% post_url 2014-02-22-Markdown %})

- &nbsp;&nbsp;[双拼输入方案：自然码简介]({% post_url 2009-11-30-zirjma %})

### # 中学文集

<div id="school-art" style="list-style-type: none;">
{% for post in site.categories.articles %}
<a href="{{ post.url }}" >&nbsp;&nbsp;{{ post.title }}</a><br/>
{% endfor %}
</div>

<!--
<ul class="listing" style="list-style-type: none;font-weight: bold;">
{% for post in {{site.categories.articles}} %}
  <li class="listing-item" style="text-indent:1em;font-weight:normal;">
  <a href="{{ post.url }}" title="{{ post.title }}" style="margin-left:1em;"><i class="fa fa-link">&nbsp;&nbsp;</i>{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
-->