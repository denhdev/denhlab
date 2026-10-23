+++
date = '2026-10-22T11:50:25-07:00'
draft = false
title = 'Typography Test'
image = '/images/placeholder-cover.svg'
tags = ['homelab', '3d-printing']
summary = 'A style test: every kind of content a post can have, so the typography can be checked in one place.'
+++

What follows on this page is a style test: various kinds of content a post can have, so the typography can be checked in one place.

The old rack was black, loud and hard to service. This rebuild prints the enclosure in white PETG and treats each node like a capsule: a standard box, four bolts, swap rather than repair.

## Parts list

Everything fits a **10-inch** frame, which keeps the footprint under a desk.

- Four mini PCs, 1U each
- An 8-port managed switch
- A patch panel, *printed in two halves*

1. Print the frame
2. Fit the cage nuts
3. Mount the nodes

### Printing the panels

Each panel prints flat in about six hours. Use `0.2 mm` layers and 4 walls.

> Print the brackets with the layer lines across the load, not along it.

```bash
kubectl get nodes -o wide
```

#### Fasteners

| Part | Size | Qty |
| --- | --- | --- |
| Cage nuts | M6 | 16 |
| Screws | M6 x 12 | 16 |

## Wiring

Run power first, then data, so the cables don't cross the airflow path.

---

That's the end of the style test.
