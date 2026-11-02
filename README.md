# denhlab

Personal site for [denhlab.com](https://denhlab.com/), built with [Hugo](https://gohugo.io/) and the [Hextra](https://github.com/imfing/hextra).

## Development

Run the dev server with live reload at <http://localhost:1313/>:

```bash
hugo server
```

Include draft posts:

```bash
hugo server -D
```

### Preview on your phone

Bind to all interfaces and point links at your machine's LAN IP (phone must be on the same network):

```bash
ip -4 -br addr                      # find your IP, e.g. 10.0.0.157
hugo server --bind 0.0.0.0 --baseURL http://10.0.0.157:1313/
```

## Writing content

```bash
hugo new blog/my-new-post.md        # new blog post (starts as draft = true)
hugo new homelab/proxmox.md         # new homelab page
```

Set `draft = false` in the front matter to publish. Optional front matter for blog cards:

```toml
image = '/images/cover.jpg'         # cover image on the card (put file in static/images/)
tags = ['homelab', 'networking']
summary = 'One-line description shown on the card.'
weight = 2                          # homelab pages: card order, lowest first
```

## Build

Build the production site into `public/`:

```bash
hugo --gc --minify
```

## Theme

Hextra is vendored in `_vendor/`, and Hugo builds from that copy. To update it, fetch the new version and re-vendor:

```bash
hugo mod get -u github.com/imfing/hextra
hugo mod tidy
hugo mod vendor
```

Three templates are copies of Hextra's with small changes, so compare them with the new versions in `_vendor/github.com/imfing/hextra/layouts/` after an update: `layouts/baseof.html` (adds the margin guides), `layouts/blog/single.html` ("Last updated" for homelab pages) and `layouts/blog/list.html` (card grid).

To customize another theme template, copy it from `_vendor/github.com/imfing/hextra/layouts/` into the same path under `layouts/` and edit the copy.
