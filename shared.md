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
ul {list-style-type: none;}

@media all and (max-width:768px){
#school-art ul {
-moz-column-count:1; /* Firefox */
-webkit-column-count:1; /* Safari and Chrome */
column-count:1;}

}
@media all and (min-width:768px){
#school-art ul {
-moz-column-count:2; /* Firefox */
-webkit-column-count:2; /* Safari and Chrome */
column-count:2;}
}
</style>  
{% endif %}
  
### # 推荐阅读

- &nbsp;&nbsp;[How to Build a GitHub Blog？]({% post_url 2016-05-16-BulidBlog %})

- &nbsp;&nbsp;[标记语言 Markdown 简明语法]({% post_url 2014-02-22-Markdown %})

- &nbsp;&nbsp;[双拼输入方案：自然码简介]({% post_url 2009-11-30-zirjma %})

### # 中学文集

<ul id="school-art">
{% for post in site.categories.articles %}
<li><a href="{{ post.url }}" >&nbsp;&nbsp;{{ post.title }}</a></li>
{% endfor %}
</ul>

<!--
<ul class="listing" style="list-style-type: none;font-weight: bold;">
{% for post in {{site.categories.articles}} %}
  <li class="listing-item" style="text-indent:1em;font-weight:normal;">
  <a href="{{ post.url }}" title="{{ post.title }}" style="margin-left:1em;"><i class="fa fa-link">&nbsp;&nbsp;</i>{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
-->