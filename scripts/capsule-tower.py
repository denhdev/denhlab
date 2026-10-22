"""Generate an isometric (axonometric) SVG of a Nakagin-style capsule tower that doubles as a homelab rack.

Composition follows a LEGO rendition of the tower, bottom to top: an octagonal podium, a dense cluster
of capsules wrapping the core, the core rising above them to a corner peak, and an antenna mast.

Units are metres, at Nakagin's real proportions: capsules 2.3 w x 3.8 l x 2.1 h, oculus 1.3 m across.
Viewer looks from +x, +y, +z, so the visible faces of any box are its +x, +y and top faces.
Face details are drawn in the face's own 2D coordinates inside an SVG matrix transform,
so circles become correct ellipses on the face plane.

Regenerate the landing page graphic after editing:
    python3 scripts/capsule-tower.py > layouts/_partials/landing/capsule-tower.html
"""
import math
import sys

S = 22  # pixels per metre
C, N = math.cos(math.radians(30)), math.sin(math.radians(30))


def P(x, y, z):
    return (S * (x - y) * C, S * ((x + y) * N - z))


def mat(a, b, c, d, origin):
    e, f = origin
    return f"matrix({a:.3f} {b:.3f} {c:.3f} {d:.3f} {e:.2f} {f:.2f})"


def face_x(X, y0, y1, z0, z1):
    """+x face at x=X. Local u runs left-to-right on screen (y1 -> y0), v runs down (z1 -> z0)."""
    return mat(S * C, -S * N, 0, S, P(X, y1, z1)), (y1 - y0, z1 - z0)


def face_y(Y, x0, x1, z0, z1):
    """+y face at y=Y. Local u runs x0 -> x1, v runs down."""
    return mat(S * C, S * N, 0, S, P(x0, Y, z1)), (x1 - x0, z1 - z0)


def face_top(Z, x0, x1, y0, y1):
    """Top face at z=Z. Local u runs x0 -> x1, v runs y0 -> y1."""
    return mat(S * C, S * N, -S * C, S * N, P(x0, y0, Z)), (x1 - x0, y1 - y0)


def group(transform, size, cls, inner=""):
    w, h = size
    return (f'<g transform="{transform}"><rect class="{cls}" width="{w:.2f}" height="{h:.2f}" />'
            f"{inner}</g>")


def polygon(cls, *points):
    """A face drawn directly from 3D points, for shapes that aren't rectangles."""
    pts = " ".join(f"{px:.2f},{py:.2f}" for px, py in (P(*pt) for pt in points))
    return f'<polygon class="{cls}" points="{pts}" />'


def line(cls, a, b):
    (x1, y1), (x2, y2) = P(*a), P(*b)
    return f'<line class="{cls}" x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" />'


def rack_holes(w, h, n):
    """Column of square mounting holes down a rack post, like rack-unit rails."""
    out = []
    step = h / (n + 1)
    for i in range(1, n + 1):
        out.append(f'<rect class="hole" x="{w / 2 - 0.09:.2f}" y="{i * step - 0.09:.2f}" width="0.18" height="0.18" />')
    return "".join(out)


def end_face(w, h, i):
    """Capsule end: the oculus, plus a row of status lights below it."""
    cx, cy, r = w / 2, h / 2 - 0.08, 0.65
    leds = "".join(
        f'<circle class="landing-led" style="--i: {i * 3 + k}" cx="{cx - 0.3 + k * 0.3:.2f}" cy="{h - 0.2:.2f}" r="0.07" />'
        for k in range(3)
    )
    return (f'<circle class="oculus" cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" />'
            f'<circle class="oculus-glass" cx="{cx:.2f}" cy="{cy:.2f}" r="{r - 0.12:.2f}" />'
            f"{leds}")


CW, CL, CH = 2.3, 3.8, 2.1   # capsule width, length, height
PER_ROW = 2                  # capsules side by side on each face of the core, per row
ROWS = 4                     # rows of capsules
CORE = CW * PER_ROW          # core footprint: wide enough for a row of capsules, flush
STACK_TOP = ROWS * CH + CH / 2
CORE_H = STACK_TOP + 3.4     # core walls rise this far above the capsules before the peak
PEAK = 5.0                   # corner peak height above the walls
MAST = 4.6                   # antenna mast height above the peak
PODIUM_H = 3.4               # podium height, below the capsules (z < 0)
PODIUM = (-2.4, CORE + 2.4)  # podium footprint extent on both axes
PODIUM_CHAMFER = 2.4


# ---- Elements: each has a bounding box (for depth sorting) and a draw function. ----

elements = []


def add(bbox, draw):
    elements.append((bbox, draw))


def draw_podium():
    a, b, k, z0, z1 = PODIUM[0], PODIUM[1], PODIUM_CHAMFER, -PODIUM_H, 0
    octagon = [(a + k, a), (b - k, a), (b, a + k), (b, b - k), (b - k, b), (a + k, b), (a, b - k), (a, a + k)]
    out = [polygon("podium-top", *[(x, y, z1) for x, y in octagon])]
    # Visible walls: +x, the +x+y chamfer, and +y. The other chamfers are edge-on or hidden.
    for (x0, y0), (x1, y1) in (((b, a + k), (b, b - k)), ((b, b - k), (b - k, b)), ((b - k, b), (a + k, b))):
        out.append(polygon("podium", (x0, y0, z0), (x1, y1, z0), (x1, y1, z1), (x0, y0, z1)))
        # A ribbon window along each wall.
        out.append(polygon("podium-window", (x0, y0, z0 + 1.2), (x1, y1, z0 + 1.2),
                           (x1, y1, z0 + 2.3), (x0, y0, z0 + 2.3)))
    return "".join(out)


add(((PODIUM[0], PODIUM[1]), (PODIUM[0], PODIUM[1]), (-PODIUM_H, 0)), draw_podium)


def draw_core():
    # The top is cut by one plane that peaks at the corner nearest the viewer and falls away along
    # both visible faces. The sloped roof faces away from the viewer, so only the walls show.
    apex = (CORE, CORE, CORE_H + PEAK)
    out = [polygon("core", (CORE, 0, 0), (CORE, CORE, 0), apex, (CORE, 0, CORE_H)),
           polygon("core", (0, CORE, 0), (CORE, CORE, 0), apex, (0, CORE, CORE_H))]
    for t, sz in (face_x(CORE, 0, CORE, 0, CORE_H), face_y(CORE, 0, CORE, 0, CORE_H)):
        out.append(f'<g transform="{t}">{rack_holes(*sz, 26)}</g>')
    # Antenna mast on the peak: a pole, crossbars, two dishes and a blinking beacon.
    x, y, z = apex
    out.append(line("mast", (x, y, z), (x, y, z + MAST)))
    for dz, half in ((1.4, 0.7), (2.6, 0.5), (3.6, 0.35)):
        out.append(line("mast", (x - half, y + half, z + dz), (x + half, y - half, z + dz)))
    for dz, side in ((1.9, -1), (3.1, 1)):
        # Offset so the dish's inner edge meets the pole.
        px, py = P(x + side * 0.26, y - side * 0.26, z + dz)
        out.append(f'<ellipse class="dish" cx="{px:.2f}" cy="{py:.2f}" rx="{0.42 * S:.2f}" ry="{0.3 * S:.2f}" />')
    bx, by = P(x, y, z + MAST)
    out.append(f'<circle class="landing-led beacon" style="--i: 0" cx="{bx:.2f}" cy="{by:.2f}" r="{0.22 * S:.2f}" />')
    return "".join(out)


add(((0, CORE), (0, CORE), (0, CORE_H + PEAK + MAST)), draw_core)


def capsule(x0, x1, y0, y1, z0, end_dir, led_index):
    """A capsule box. end_dir is the axis its oculus faces ('x' or 'y'), or None if that end is hidden."""
    z1 = z0 + CH

    def draw():
        out = [group(*face_top(z1, x0, x1, y0, y1), "cap-top")]
        fx, fy = face_x(x1, y0, y1, z0, z1), face_y(y1, x0, x1, z0, z1)
        out.append(group(*fx, "cap", end_face(*fx[1], led_index) if end_dir == "x" else ""))
        out.append(group(*fy, "cap", end_face(*fy[1], led_index) if end_dir == "y" else ""))
        return "".join(out)

    add(((x0, x1), (y0, y1), (z0, z1)), draw)


# Capsules. Those projecting along x sit on whole rows; those along y are offset half a capsule,
# giving Nakagin's staggered stack. Every face of the core carries PER_ROW capsules per row, and the
# +x face carries one extra that overhangs into the front corner, so the cluster reads as one mass.
n = 0
for row in range(ROWS):
    zx, zy = row * CH, row * CH + CH / 2
    for slot in range(PER_ROW + 1):                       # +x face, plus the front-corner capsule
        a0, a1 = slot * CW, (slot + 1) * CW
        capsule(CORE, CORE + CL, a0, a1, zx, "x", n); n += 1
    for slot in range(PER_ROW):
        a0, a1 = slot * CW, (slot + 1) * CW
        capsule(-CL, 0, a0, a1, zx, None, 0)              # -x face: end faces away
        capsule(a0, a1, CORE, CORE + CL, zy, "y", n); n += 1  # +y face
        capsule(a0, a1, -CL, 0, zy, None, 0)              # -y face: end faces away


# ---- Depth sort: draw an element after everything behind it. ----

def behind(a, b):
    """True if box a is definitely behind box b along some axis and in front along none."""
    votes = set()
    for (a0, a1), (b0, b1) in zip(a, b):
        if a1 <= b0 + 1e-9:
            votes.add("a")
        elif b1 <= a0 + 1e-9:
            votes.add("b")
    return votes == {"a"}


order, remaining = [], list(range(len(elements)))
while remaining:
    ready = [i for i in remaining if not any(behind(elements[j][0], elements[i][0]) for j in remaining if j != i)]
    if not ready:  # cyclic overlap: fall back to the lowest, farthest element
        ready = [min(remaining, key=lambda i: (elements[i][0][2][0], sum(r[0] for r in elements[i][0][:2])))]
    pick = min(ready, key=lambda i: (elements[i][0][2][0], sum(r[0] for r in elements[i][0][:2])))
    order.append(pick)
    remaining.remove(pick)

parts = [elements[i][1]() for i in order]

# Bounds for the viewBox, from every element's box corners.
xs, ys = [], []
for (xr, yr, zr), _ in elements:
    for x in xr:
        for y in yr:
            for z in zr:
                px, py = P(x, y, z)
                xs.append(px)
                ys.append(py)
pad = 10
vb = (min(xs) - pad, min(ys) - pad, max(xs) - min(xs) + 2 * pad, max(ys) - min(ys) + 2 * pad)

svg = ("<!-- Generated by scripts/capsule-tower.py; edit that and regenerate rather than editing here. -->\n"
       f'<svg viewBox="{vb[0]:.0f} {vb[1]:.0f} {vb[2]:.0f} {vb[3]:.0f}" xmlns="http://www.w3.org/2000/svg">\n  '
       + "\n  ".join(parts) + "\n</svg>\n")
sys.stdout.write(svg)
