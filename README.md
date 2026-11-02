# denhlab

Personal site for [denhlab.com](https://denhlab.com/), built with [Hugo](https://gohugo.io/) and the [Hextra](https://github.com/imfing/hextra) theme (a Hugo module, vendored into `_vendor/` so builds don't need Go).

## Layout

| Path | What it is |
| --- | --- |
| `content/_index.md` | Landing page text: headline, tagline, CTA and blog links, and the "Lately" ticker items |
| `content/blog/` | Blog posts, listed as cards at `/blog/` |
| `content/homelab/` | Homelab pages, shown as cards like the blog, ordered by `weight`, with "Last updated" instead of dates |
| `data/homelab/` | Hardware timeline, certifications timeline and Kubestronaut progress (YAML, newest first) |
| `layouts/home.html` | Landing page template and rack drawing |
| `layouts/baseof.html` | Copy of Hextra's base template with the margin guides added |
| `layouts/blog/list.html`, `single.html` | Card grid and post page (override Hextra's) |
| `layouts/_shortcodes/` | Elevation drawings (`rack-elevation`, `core-v1-elevation`, `t480-elevation`), `timeline` and `kubestronaut` |
| `layouts/_partials/sheet-guides.html` | Margin guides on every page |
| `layouts/_markup/render-table.html` | Tables that stack into cards on phones (five or more columns) |
| `assets/css/custom.css` | All site styles: drawings, landing page, cards, timeline, tables |
| `assets/css/typesets/` | Font sets (pick one with `typeset` in `hugo.toml`) |
| `assets/css/palettes/` | Color sets for light and dark mode (pick one with `palette` in `hugo.toml`) |
| `static/fonts/` | Self-hosted font files used by the typesets |
| `static/images/` | Card covers; SVG covers are inlined so they follow light and dark mode |
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

The site uses one of the font sets in `assets/css/typesets/`, chosen in `hugo.toml`:

```toml
[params]
  typeset = 'editorial'   # 'swiss', 'editorial', 'technical', 'bauhaus' or 'poster'
```

Try one without editing the config:

```bash
HUGO_PARAMS_TYPESET=bauhaus hugo server
```

To add a typeset, copy one of the files, change its `@font-face` rules and `--type-*` variables, put its font files in `static/fonts/`, and set `typeset` to the new file name.

## Palettes

All site colors come from one of the palettes in `assets/css/palettes/`, chosen in `hugo.toml`:

```toml
[params]
  palette = 'mono'
```

Each palette defines the same set of colors twice: dark mode under `html.dark`, light mode under `:root`. `custom.css` only refers to these names (`--color-bg`, `--color-fg`, `--site-accent`, …) and never names a color directly. Try one without editing the config:

```bash
HUGO_PARAMS_PALETTE=mono hugo server
```

To add a palette, copy `mono.css`, change its values in both modes, and set `palette` to the new file name.

## Landing page

Everything on the landing page is set in `content/_index.md`. The ticker along the bottom reads its label and items from there:

```toml
  nowPlayingLabel = 'Lately'
  [[params.nowPlaying]]
    kind = 'Album'
    title = 'Parallel – Overwerk'
```

## Homelab data

The hardware and certifications timelines are drawn from `data/homelab/timeline.yaml` and `data/homelab/certifications.yaml`. Add entries newest first; amounts are positive for money in and negative for money out, and the totals add themselves up. Mark a certification passed in `data/homelab/kubestronaut.yaml` and the progress bar follows.

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
