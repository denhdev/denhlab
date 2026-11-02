+++
title = 'Homelab'
# Cards follow each page's weight (lowest first) rather than its date.
[params]
  sortBy = 'weight'
  sortOrder = 'asc'
# Render this section like the blog: a grid of cards here, and each page as a post.
# hideDate leaves dates off the cards, and posts show "Last updated <month>" from lastmod instead
# of the publish date; front matter dates still set the card order.
[[cascade]]
  type = 'blog'
  [cascade.params]
    hideDate = true
+++

Hardware, services, and notes on how the homelab is put together.
