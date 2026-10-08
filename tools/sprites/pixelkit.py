"""Tiny pixel-art construction kit for the original Mochiichao sprite set.

Shapes are rasterised as boolean masks on a 96x96 grid, layered in order, then
auto-shaded (light from the upper-left) and auto-outlined (selective dark
outline per material). Every sprite in the set goes through the same pipeline
so the set stays visually consistent. No external art is used.
"""
import math
import numpy as np
from PIL import Image

W = H = 96
YY, XX = np.mgrid[0:H, 0:W].astype(float)


def hexc(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


class Ramp:
    """outline, shadow, base, light (+ optional highlight)."""
    def __init__(self, *cols):
        self.c = [hexc(c) for c in cols]
        self.outline, self.shadow, self.base, self.light = self.c[:4]
        self.hi = self.c[4] if len(self.c) > 4 else self.c[3]


# ---------------------------------------------------------------- masks
def ellipse(cx, cy, rx, ry, rot=0.0):
    a = math.radians(rot)
    x, y = XX + 0.5 - cx, YY + 0.5 - cy
    xr = x * math.cos(a) + y * math.sin(a)
    yr = -x * math.sin(a) + y * math.cos(a)
    return (xr / rx) ** 2 + (yr / ry) ** 2 <= 1.0


def circle(cx, cy, r):
    return ellipse(cx, cy, r, r)


def rect(x0, y0, x1, y1):
    return (XX >= x0) & (XX < x1) & (YY >= y0) & (YY < y1)


def poly(pts):
    px, py = XX + 0.5, YY + 0.5
    inside = np.zeros((H, W), bool)
    n = len(pts)
    j = n - 1
    for i in range(n):
        xi, yi = pts[i]; xj, yj = pts[j]
        cond = ((yi > py) != (yj > py)) & (px < (xj - xi) * (py - yi) / ((yj - yi) or 1e-9) + xi)
        inside ^= cond
        j = i
    return inside


def capsule(x0, y0, x1, y1, r0, r1=None):
    r1 = r0 if r1 is None else r1
    px, py = XX + 0.5, YY + 0.5
    dx, dy = x1 - x0, y1 - y0
    L2 = dx * dx + dy * dy or 1e-9
    t = np.clip(((px - x0) * dx + (py - y0) * dy) / L2, 0, 1)
    d = np.hypot(px - (x0 + t * dx), py - (y0 + t * dy))
    return d <= r0 + (r1 - r0) * t


def chain(pts, r0, r1=None):
    """tapering polyline of capsules."""
    r1 = r0 if r1 is None else r1
    m = np.zeros((H, W), bool)
    n = len(pts) - 1
    for i in range(n):
        ra = r0 + (r1 - r0) * i / n
        rb = r0 + (r1 - r0) * (i + 1) / n
        m |= capsule(*pts[i], *pts[i + 1], ra, rb)
    return m


def wave_band(y0, amp, period, thick, phase=0.0):
    return np.abs(YY + 0.5 - (y0 + amp * np.sin((XX + 0.5) / period + phase))) <= thick / 2


def ring(cx, cy, rx, ry, t, rot=0.0):
    return ellipse(cx, cy, rx, ry, rot) & ~ellipse(cx, cy, max(rx - t, .1), max(ry - t, .1), rot)


def crescent(cx, cy, r, ox, oy, r2=None):
    return circle(cx, cy, r) & ~circle(cx + ox, cy + oy, r if r2 is None else r2)


def line(x0, y0, x1, y1, t=1.0):
    return capsule(x0, y0, x1, y1, t / 2)


# ---------------------------------------------------------------- canvas
class Sprite:
    def __init__(self):
        self.parts = []  # (mask, ramp, kind, opts)

    def add(self, mask, ramp, shade=True, outline=True, sh=2):
        """A solid body part: shaded + outlined."""
        self.parts.append(dict(mask=mask.copy(), ramp=ramp, kind='part', shade=shade, outline=outline, sh=sh))
        return mask

    def paint(self, mask, color, clip=None):
        """Flat detail painted onto whatever is beneath (no outline/shade).
        clip: restrict to pixels already covered."""
        self.parts.append(dict(mask=mask.copy(), color=hexc(color) if isinstance(color, str) else color,
                               kind='paint', clip=clip))

    def render(self):
        img = np.zeros((H, W, 4), np.uint8)
        owner = -np.ones((H, W), int)
        order = []
        for i, p in enumerate(self.parts):
            m = p['mask']
            if p['kind'] == 'part':
                r = p['ramp']
                col = np.zeros((H, W, 4), np.uint8)
                col[:] = r.base
                if p['shade']:
                    s = p['sh']
                    # shadow where the part ends towards lower-right, light toward upper-left
                    sh = np.zeros_like(m)
                    sh[:-s, :-s] = ~m[s:, s:]
                    sh[-s:, :] = True; sh[:, -s:] = True
                    lt = np.zeros_like(m)
                    lt[1:, 1:] = ~m[:-1, :-1]
                    lt[0, :] = True; lt[:, 0] = True
                    lt2 = np.zeros_like(m)
                    lt2[2:, 2:] = ~m[:-2, :-2]
                    col[m & lt2] = r.light
                    col[m & lt] = r.hi
                    col[m & sh & ~lt] = r.shadow
                img[m] = col[m]
                # interior outline: this part's edge pixels that sit over an earlier part
                if p['outline']:
                    edge = np.zeros_like(m)
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nb = shift(m, dy, dx, True)
                        edge |= m & ~nb
                    over = edge & (owner >= 0)
                    img[over] = r.outline
                owner[m] = i
                order.append(i)
            else:
                mm = m & (owner >= 0) if p.get('clip', True) is not False else m
                if p.get('clip') is False:
                    mm = m
                img[mm] = p['color']
                owner[mm & (owner < 0)] = i
        # exterior outline: transparent pixels next to an opaque one take the
        # owner's outline colour
        alpha = img[..., 3] > 0
        out = img.copy()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb_alpha = shift(alpha, dy, dx, False)
            nb_owner = shift(owner, dy, dx, -1)
            tgt = ~alpha & nb_alpha & (out[..., 3] == 0) & (nb_owner >= 0)
            ys, xs = np.nonzero(tgt)
            for y, x in zip(ys, xs):
                p = self.parts[nb_owner[y, x]]
                if p['kind'] == 'part' and p['outline']:
                    out[y, x] = p['ramp'].outline
                elif p['kind'] == 'paint':
                    out[y, x] = darker(p['color'])
        return Image.fromarray(out, 'RGBA')


def shift(a, dy, dx, fill=False):
    """non-wrapping np.roll replacement (pixels shifted in from outside = fill)."""
    out = np.full_like(a, fill)
    H_, W_ = a.shape[:2]
    ys = slice(max(dy, 0), H_ + min(dy, 0)); yd = slice(max(-dy, 0), H_ + min(-dy, 0))
    xs = slice(max(dx, 0), W_ + min(dx, 0)); xd = slice(max(-dx, 0), W_ + min(-dx, 0))
    out[ys, xs] = a[yd, xd]
    return out


def darker(c, f=0.35):
    return (int(c[0] * f), int(c[1] * f), int(c[2] * f), 255)


def flip(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)
