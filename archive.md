---
layout: page
title: "Lifeline"
description: "生命在这里留下轨迹"
header-img: "img/orange.jpg"
---


<ul class="listing" style="list-style-type:none;">
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator">{{ y }}</li>
  {% endif %}
  <li class="listing-item" style="text-indent:3em;">
    <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%m/%d" }}</time>
    <a href="{{ post.url }}" title="{{ post.title }}" style="margin-left:1.5em;">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
