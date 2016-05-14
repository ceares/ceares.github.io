---
layout: page
title: "Tags"
description: "不要随意贴人标签"  
header-img: "img/semantic.jpg"  
---

<div id='tag_cloud' style="margin:0.5in 0em;font-weight: normal;">
{% for tag in site.tags %}
<a href="#{{ tag[0] }}" title="{{ tag[0] }}" rel="{{ tag[1].size }}" style="margin-right:1em;"><i class="fa fa-tag">&nbsp;{{ tag[0] }}</i></a>
{% endfor %}
</div>

> <i class="fa fa-spinner">&nbsp;</i>Matching Gene…

<ul class="listing" style="list-style-type: none;font-weight: bold;margin-top:0.5in;">
{% for tag in site.tags %}
  <li class="listing-seperator" id="{{ tag[0] }}">{{ tag[0] }}</li>
{% for post in tag[1] %}
  <li class="listing-item" style="text-indent:3em;font-weight:normal;">
  <!--<time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y/%m/%d" }}</time>-->
  <a href="{{ post.url }}" title="{{ post.title }}" style="margin-left:1em;">{{ post.title }}</a>
  </li>
{% endfor %}
{% endfor %}
</ul>

<script src="/media/js/jquery.tagcloud.js" type="text/javascript" charset="utf-8"></script> 
<script language="javascript">
$.fn.tagcloud.defaults = {
    size: {start: 1, end: 1, unit: 'em'},
      color: {start: '#f8e0e6', end: '#ff3333'}
};

$(function () {
    $('#tag_cloud a').tagcloud();
});
</script>
