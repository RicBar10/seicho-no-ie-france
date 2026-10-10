# Décors « nature » en SVG (arbres, collines, branches, feuilles), dessinés pour le site.
import random

def _pine(x, base, h, color):
    w = h * 0.42
    p = []
    for i in range(3):
        top = base - h + i * h * 0.22
        bot = base - h * 0.18 - (2 - i) * h * 0.18 + i * 0
        bw = w * (0.55 + i * 0.25)
        p.append(f'<path d="M{x:.1f} {top:.1f} L{x+bw/2:.1f} {top + h*0.42:.1f} L{x-bw/2:.1f} {top + h*0.42:.1f}Z" fill="{color}"/>')
    p.append(f'<rect x="{x-h*0.03:.1f}" y="{base-h*0.16:.1f}" width="{h*0.06:.1f}" height="{h*0.16:.1f}" fill="{color}"/>')
    return "".join(p)

def _round(x, base, h, color):
    r = h * 0.32
    return (f'<rect x="{x-h*0.035:.1f}" y="{base-h*0.45:.1f}" width="{h*0.07:.1f}" height="{h*0.45:.1f}" fill="{color}"/>'
            f'<circle cx="{x:.1f}" cy="{base-h+r:.1f}" r="{r:.1f}" fill="{color}"/>'
            f'<circle cx="{x-r*0.7:.1f}" cy="{base-h+r*1.6:.1f}" r="{r*0.75:.1f}" fill="{color}"/>'
            f'<circle cx="{x+r*0.7:.1f}" cy="{base-h+r*1.6:.1f}" r="{r*0.75:.1f}" fill="{color}"/>')

def forest(seed=3, height=170, layers=(("#cfe3c2", 0.9, 70, 90), ("#b6d6a4", 0.95, 95, 130), ("#9cc68a", 1, 120, 160))):
    """Lisière de forêt en trois plans, du plus clair (lointain) au plus soutenu."""
    rnd = random.Random(seed)
    W = 1440
    out = []
    for li, (col, op, hmin, hmax) in enumerate(layers):
        base = height - 8 + li * 3
        # colline
        y0 = base - 20 - li * 6
        out.append(f'<path d="M0 {y0} C 240 {y0-30} 480 {y0+18} 720 {y0-8} S 1200 {y0-26} 1440 {y0} V {height} H 0Z" fill="{col}" opacity="{op}"/>')
        x = rnd.uniform(-20, 40)
        while x < W + 40:
            h = rnd.uniform(hmin, hmax) * (height / 170)
            if li == 2 and rnd.random() < 0.6:
                x += rnd.uniform(60, 160); continue  # premier plan plus clairsemé
            f = _pine if rnd.random() < 0.55 else _round
            out.append(f'<g opacity="{op}">{f(x, y0 + 14, h, col)}</g>')
            x += rnd.uniform(28, 70) * (1.6 if li == 2 else 1)
    return (f'<svg class="forest" viewBox="0 0 {W} {height}" preserveAspectRatio="xMidYMax slice" aria-hidden="true">'
            + "".join(out) + "</svg>")

def branch(cls="branch", flip=False, seed=1, color="#7fae69", leaves=9):
    """Branche feuillue qui descend d'un coin."""
    rnd = random.Random(seed)
    pts = [(0, 0), (60, 40), (120, 70), (190, 92), (260, 104)]
    d = "M0 0 C 70 40, 150 90, 260 104"
    out = [f'<path d="{d}" stroke="{color}" stroke-width="3" fill="none" stroke-linecap="round"/>']
    for i in range(leaves):
        t = (i + 1) / (leaves + 1)
        # point approximatif sur la courbe
        x = 260 * t; y = 104 * (1 - (1 - t) ** 1.6)
        side = -1 if i % 2 else 1
        ang = 25 + side * 45 + rnd.uniform(-10, 10)
        size = 18 + rnd.uniform(-3, 6) - t * 4
        shade = ["#8dbb73", "#a3c98a", "#76a862", "#b5d39b"][i % 4]
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{size:.1f}" ry="{size*0.38:.1f}" fill="{shade}" '
                   f'transform="rotate({ang:.0f} {x:.1f} {y:.1f}) translate({size*0.9:.1f} 0)"/>')
    tr = ' style="transform:scaleX(-1)"' if flip else ""
    return f'<svg class="{cls}" viewBox="-20 -30 310 170" aria-hidden="true"{tr}>' + "".join(out) + "</svg>"

SPRIG = ('<svg class="sprig" viewBox="0 0 120 24" aria-hidden="true">'
         '<path d="M4 12 H116" stroke="#d9b45c" stroke-width="1.2"/>'
         '<ellipse cx="52" cy="8" rx="7" ry="3" fill="#8dbb73" transform="rotate(-30 52 8)"/>'
         '<ellipse cx="68" cy="8" rx="7" ry="3" fill="#a3c98a" transform="rotate(30 68 8)"/>'
         '<ellipse cx="60" cy="5" rx="6" ry="2.6" fill="#76a862" transform="rotate(90 60 5)"/>'
         '<circle cx="60" cy="12" r="2.6" fill="#e9b54a"/></svg>')

LEAF_ICON = ('<svg class="leaf-ico" viewBox="0 0 24 24" aria-hidden="true">'
             '<path d="M5 19 C5 9 11 4 20 4 C20 13 15 19 5 19Z" fill="#a3c98a"/>'
             '<path d="M5 19 L15 9" stroke="#5f9a4d" stroke-width="1.4" stroke-linecap="round"/></svg>')
