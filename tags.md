---
layout: page
title: "Tags"
description: "不要随意贴人标签"  
header-img: "img/semantic.jpg"  
---

<style type="text/css">
@media all and (max-width:768px){
#tag_cloud {margin:0.5in 0em;font-weight: normal;
-moz-column-count:3; /* Firefox */
-webkit-column-count:3; /* Safari and Chrome */
column-count:3;}
#tag_cloud a{margin-right:5em}
}
@media all and (min-width:768px){
#tag_cloud {margin:0.5in 0em;font-weight: normal;
-moz-column-count:5; /* Firefox */
-webkit-column-count:5; /* Safari and Chrome */
column-count:5;}
#tag_cloud a{margin-right:5em}
}
#MatchingGene {font-style:italic;color:gray;margin:0em 1em 0.5in}
</style>

<div id='tag_cloud'>
{% for tag in site.tags %}
<a href="#{{ tag[0] }}" title="{{ tag[0] }}" rel="{{ tag[1].size }}"><i class="fa fa-tags" style="color:#11b7ae">&nbsp;&nbsp;</i>{{ tag[0] }}</a><br/>
{% endfor %}
</div>

<div id="MatchingGene"><i class="fa fa-spinner fa-pulse"></i> &nbsp; Matching Gene</div>

<ul class="listing" style="list-style-type: none;font-weight: bold;">
{% for tag in site.tags %}
  <li class="listing-seperator" id="{{ tag[0] }}" style="margin:1em auto">#&nbsp;{{ tag[0] }}</li>
{% for post in tag[1] %}
  <li class="listing-item" style="text-indent:1em;font-weight:normal;">
  <!--<time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y/%m/%d" }}</time>-->
  <a href="{{ post.url }}" title="{{ post.title }}" style="margin-left:1em;"><i class="fa fa-link">&nbsp;&nbsp;</i>{{ post.title }}</a>
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
