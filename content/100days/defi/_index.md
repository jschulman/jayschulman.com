---
title: "100 Days of Blockchain"
description: "Join me on a 100-day journey exploring the world of blockchain and digital assets."
---

Welcome to my "100 Days of Blockchain" series! Over the next 100 days, I will be diving deep into various aspects of blockchain technology and digital assets.

<section class="posts">
  {{ range .Pages }}
    <article class="post">
      <h2><a href="{{ .Permalink }}">{{ .Title }}</a></h2>
      <p class="date">{{ .Date.Format "January 2, 2006" }}</p>
      <p>{{ .Summary }}</p>
      <a href="{{ .Permalink }}" class="read-more">Read more...</a>
    </article>
  {{ end }}
</section>
