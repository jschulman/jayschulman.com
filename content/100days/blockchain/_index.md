---
title: "100 Days of Blockchain"
description: "Explore 100 short lessons on blockcchain."
---

{{ range .Pages }}
  <article class="post">
    <h2><a href="{{ .Permalink }}">{{ .Title }}</a></h2>
    <p class="date">{{ .Date.Format "January 2, 2006" }}</p>
    <p>{{ .Summary }}</p>
    <a href="{{ .Permalink }}" class="read-more">Read more...</a>
  </article>
{{ end }}
