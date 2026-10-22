# denhlab

Personal site for [denhlab.com](https://denhlab.com/), built with [Hugo](https://gohugo.io/) and the [Hextra](https://github.com/imfing/hextra) theme (pulled in as a Hugo module).

## Layout

| Path | What it is |
| --- | --- |
| `content/_index.md` | Landing page text (headline, tagline, CTA) |
| `content/blog/` | Blog posts, listed as cards at `/blog/` |
| `content/homelab/` | Homelab section (Hextra docs layout with sidebar) |
| `layouts/home.html` | Landing page template and hero graphic |
| `layouts/blog/list.html` | Blog card grid (overrides Hextra's list) |
| `assets/css/custom.css` | Styles for the landing page and blog cards |
| `assets/css/typesets/` | Font sets for the landing page and cards (pick one with `typeset` in `hugo.toml`) |
| `static/fonts/` | Self-hosted font files used by the typesets |
| `hugo.toml` | Site config and navbar / mobile menu entries |

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

Then open `http://10.0.0.157:1313/` on the phone. If it won't load, open the port in Fedora's firewall (lasts until reboot; add `--permanent` to keep it):

```bash
sudo firewall-cmd --add-port=1313/tcp
```

## Typesets

The landing page and blog cards use one of the font sets in `assets/css/typesets/`, chosen in `hugo.toml`:

```toml
[params]
  typeset = 'swiss'    # 'swiss', 'editorial', 'technical' or 'bauhaus'
```

Try one without editing the config:

```bash
HUGO_PARAMS_TYPESET=bauhaus hugo server
```

To add a typeset, copy one of the files, change its `@font-face` rules and `--type-*` variables, put its font files in `static/fonts/`, and set `typeset` to the new file name.

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
```

## Build

Build the production site into `public/`:

```bash
hugo --gc --minify
```

## Theme

Update Hextra to the latest version:

```bash
hugo mod get -u github.com/imfing/hextra
hugo mod tidy
```

Hextra's source lives in the Hugo module cache (`hugo config | grep cachedir`). To customize a theme template, copy it from there into the same path under `layouts/` and edit the copy.
