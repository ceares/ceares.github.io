---
layout: page
title: "Tags"
description: "不要随意贴人标签"  
header-img: "rgba(17,181,174,1)" 
custom_css_tags: true 
nav-display: true
---


{% if page.custom_css_tags %}
<style type="text/css">
#tag_cloud {margin:0.5in 0em;font-weight: normal;}
@media all and (max-width: 500px){
	#tag_cloud {
	-moz-column-count:2; /* Firefox */
	-webkit-column-count:2; /* Safari and Chrome */
	column-count:2;}
}
@media all and (min-width:500px) and (max-width:750px){
	#tag_cloud {
	-moz-column-count:3; /* Firefox */
	-webkit-column-count:3; /* Safari and Chrome */
	column-count:3;}
}
@media all and (min-width:750px) and (max-width: 1000px){
	#tag_cloud {
	-moz-column-count:4; /* Firefox */
	-webkit-column-count:4; /* Safari and Chrome */
	column-count:4;}
}
@media all and (min-width:1000px){
	#tag_cloud {
	-moz-column-count:5; /* Firefox */
	-webkit-column-count:5; /* Safari and Chrome */
	column-count:5;}
}
#MatchingGene {font-style:italic;color:#0590f0;margin:0em 1em 0.5in}
#MyTags {color:lightgray} 
#tag-sup {font-size:14px;color:#0590f0}
.listing-seperator {	margin:1em auto;}
.listing-item{font-weight:normal;}
@media all and (max-width:768px){
.listing-item{text-indent:0em;}
.listing {margin-left: -2em;}
}
@media all and (min-width:768px){
.listing-item{text-indent:2em;}
}
</style>
{% endif %}

<div id='tag_cloud'>
{% for tag in site.tags  %}
<a href="#{{ tag[0] }}" title="{{ tag[0] }}" rel="{{ tag[1].size }}"><i id="MyTags" class="fa fa-tags">&nbsp;&nbsp;</i> {{ tag[0] }} <sup id="tag-sup"> {{ tag[1].size }} </sup> </a><br/>
{% endfor %}
</div>

<div id="MatchingGene"><i class="fa fa-spinner fa-pulse"></i> &nbsp; Matching Gene</div>

<ul class="listing" style="list-style-type: none;font-weight: bold;">
{% for tag in site.tags %}
  <li class="listing-seperator" id="{{ tag[0] }}" >#&nbsp;{{ tag[0] }}</li>
{% for post in tag[1] %}
  <li class="listing-item" >
  <a href="{{ post.url }}" title="{{ post.title }}" style="margin-left:1em;"><i class="fa fa-link">&nbsp;&nbsp;</i>{{ post.title }}</a>
  </li>
{% endfor %}
{% endfor %}
</ul>

<!--
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
-->