"""Hand-authored, part-based pixel designs for every Mochiichao species.

Each design is a function draw(s, back) that layers shapes from pixelkit onto a
96x96 Sprite. `back=True` omits face/belly detail and adds back-side markings;
the build script mirrors back sprites so they face the opponent.
All designs are original; colours come from the owner's per-species colours
(species_table.py) and the game's element palette.
"""
from pixelkit import *

def R(*c): return Ramp(*c)
# ---------------------------------------------------------------- palette (element ramps)
MOCHI   = R('#0d3b52', '#2a86b0', '#4fc3f7', '#a6e6ff', '#e6f9ff')
AQUA    = R('#0b3a4a', '#1f7f9a', '#3fb6d3', '#8ee3f2', '#d4f7fc')
DEEPBLU = R('#04203d', '#013a6b', '#01579b', '#2f86c9', '#7cc4ec')
FOAM    = R('#2a5a6a', '#a6d8e6', '#e6f9ff', '#ffffff')
SASH    = R('#070f2a', '#121f4a', '#1a2f6e', '#3550a0')
CHROME  = R('#232a33', '#5b6875', '#90a4ae', '#cfd8dc', '#ffffff')
BRIGHTCH= R('#2a3038', '#7d8b97', '#cfd8dc', '#f2f6f8', '#ffffff')
GUNMET  = R('#101418', '#2a323b', '#4f5b66', '#7d8b97', '#a9b6c0')
UNDERGR = R('#06200a', '#103d17', '#1b5e20', '#2e7d32')
TEAL    = R('#06352f', '#11867a', '#2dd4bf', '#99f6e4')
EARTH   = R('#2e1c10', '#6b4428', '#9a6b42', '#c79a6b', '#e2c09a')
SAND    = R('#3d2a12', '#9c7136', '#d4a35a', '#f0cf8f')
BONE    = R('#3a3428', '#a89e88', '#e6dcc4', '#fffaf0')
STONE   = R('#24221f', '#5a5650', '#8a857b', '#b9b3a6', '#dcd7cb')
DKSTONE = R('#151412', '#34312d', '#5a5650', '#7f7a70')
FLAME   = R('#4a1405', '#b8420f', '#f08030', '#ffc061', '#fff1b0')
EMBER   = R('#5a1a00', '#e0561a', '#ff9a2e', '#ffe08a')
LAV     = R('#2d1640', '#7e4d99', '#ce93d8', '#f1d5f7')
UMBRAL  = R('#140a24', '#3a2160', '#705898', '#a98ccf')
VOID    = R('#05040a', '#141420', '#262636', '#3d3d55')
WISP    = R('#2a1a4a', '#6f58a8', '#b39ddb', '#e9e0ff')
FLORA   = R('#12301a', '#2f6e3a', '#5aa85a', '#8fd18f')
MINT    = R('#1b3b2a', '#4f8f6b', '#a5d6a7', '#dff3e0')
MOSS    = R('#16260f', '#35571f', '#5e8a2e', '#8db850')
SILK    = R('#3b3a2c', '#a39f88', '#e8e4d0', '#ffffff')
LIME    = R('#2a3a14', '#7a9a4a', '#c5e1a5', '#eef7e0')
SKY     = R('#163a52', '#4f8fb8', '#b3e5fc', '#eaf8ff')
FALCON  = R('#0f2c45', '#3d7fb0', '#7cc4ec', '#c8ecff')
WHITE   = R('#3a4a5a', '#b8c8d8', '#f4f8fc', '#ffffff')
STORM   = R('#0e1420', '#2b3850', '#4a5d7e', '#7d92b5')
PEACH   = R('#4a2a10', '#c2884a', '#ffcc80', '#ffecc8')
TAN     = R('#40240c', '#a8723c', '#e0a868', '#f6d2a0')
CORAL   = R('#4a1a10', '#c45a42', '#ffab91', '#ffe0d4')
NAVY    = R('#060a24', '#121a5e', '#1a237e', '#3d4ab8')
INDIGO  = R('#04061a', '#0b1040', '#121a5e', '#26318f')
INK     = R('#05050a', '#141420', '#262636', '#4a4a66')
TOXIC   = R('#1c0a2a', '#5a2a7a', '#9a4ac0', '#d08cf0')
PINK    = R('#4a0f33', '#c23d8f', '#ff66cc', '#ffb8e8')
GLITCH  = R('#063a24', '#10a060', '#22ff99', '#b0ffd8')
NEONPK  = R('#3a0a2a', '#b0287a', '#ff4fb0', '#ffb0e0')
GOLD    = R('#4a3300', '#b8860b', '#ffd700', '#fff3a0', '#ffffff')
IVORY   = R('#5a5040', '#d8ccb0', '#fffaf0', '#ffffff')
VIOLET  = R('#1e0f3a', '#4b2b8a', '#7e57c2', '#b39ddb')
ORANGE  = R('#4a1a00', '#c25a10', '#ff8c2a', '#ffc27a')
YELLOW  = R('#3a3a00', '#a8a800', '#e6e600', '#ffff99')
RAG     = R('#3a200c', '#8a5a2a', '#c2884a', '#e8b880')
CYANGLW = '#2dffd2'; NEONGRN = '#39ff7a'; NEONYEL = '#f6ff4a'; HOTPINK = '#ff4fb0'; RED = '#ff2a6d'
EYE = '#141018'; GLINT = '#ffffff'

# ---------------------------------------------------------------- helpers
def eye(s, x, y, rx=2.2, ry=2.8, col=EYE, glint=True, white=False):
    if white:
        s.paint(ellipse(x, y, rx + 1.2, ry + 1.0), '#ffffff')
    s.paint(ellipse(x, y, rx, ry), col)
    if glint:
        s.paint(rect(int(x - rx * 0.6), int(y - ry * 0.6), int(x - rx * 0.6) + 1, int(y - ry * 0.6) + 1), GLINT)

def eyes(s, cx, y, sep, **k):
    eye(s, cx - sep, y, **k); eye(s, cx + sep, y, **k)

def glow_eye(s, x, y, w, col):
    s.paint(rect(x, y, x + w, y + 2), col)

def mouth(s, x, y, w=4, col='#1a0f14'):
    s.paint(rect(x - w // 2, y, x - w // 2 + w, y + 1), col)

def fangs(s, x, y, n=2, gap=4, col='#ffffff'):
    for i in range(n):
        xx = int(x + (i - (n - 1) / 2) * gap)
        s.paint(poly([(xx - 1, y), (xx + 2, y), (xx + 0.5, y + 3)]), col, clip=False)

def spikes(s, pts, ramp, h=6, w=4, up=(0, -1)):
    for (x, y) in pts:
        ux, uy = up
        s.add(poly([(x - w / 2, y), (x + w / 2, y), (x + ux * h, y + uy * h)]), ramp)

def dots(s, pts, r, col):
    for x, y in pts: s.paint(circle(x, y, r), col)

def shadow_none(): pass

# ---------------------------------------------------------------- AQUA line
def mochii(s, back):
    # squat mochi-dumpling body, flat base, a rolling wave-curl on top
    s.add(ellipse(37, 85, 6, 4), MOCHI); s.add(ellipse(59, 85, 6, 4), MOCHI)
    body = ellipse(48, 70, 22, 17) | rect(27, 70, 70, 84) & ellipse(48, 72, 22, 14)
    s.add(body, MOCHI)
    s.add(crescent(50, 50, 7, 3, 3, 5.5) | circle(45, 53, 3.2), MOCHI)          # wave curl
    s.paint(wave_band(76, 2, 3.2, 2.0), MOCHI.light)
    s.paint(wave_band(80, 2, 3.2, 1.6, 1.6), MOCHI.shadow)
    if back:
        s.paint(wave_band(64, 2, 3.2, 2.0, .8), MOCHI.light)
        return
    eyes(s, 48, 66, 8, rx=2.6, ry=3.4)
    s.paint(ellipse(36, 72, 2.6, 1.6), '#a6e6ff'); s.paint(ellipse(60, 72, 2.6, 1.6), '#a6e6ff')
    s.paint(rect(46, 72, 51, 73), MOCHI.outline)

def tiidebiite(s, back):
    # water martial artist: wide stance, gi sash, water rings on the fists, wave-crest hair
    s.add(capsule(40, 66, 34, 86, 5), AQUA); s.add(capsule(56, 66, 62, 86, 5), AQUA)   # legs
    s.add(ellipse(33, 88, 6, 3), AQUA); s.add(ellipse(63, 88, 6, 3), AQUA)
    s.add(ellipse(48, 58, 13, 15), AQUA)                                              # torso
    s.add(rect(35, 62, 61, 67) & ellipse(48, 60, 14, 16), SASH)                        # sash
    s.add(poly([(58, 64), (64, 64), (66, 75), (61, 74)]), SASH)
    s.add(capsule(37, 50, 24, 60, 4), AQUA); s.add(capsule(59, 50, 72, 60, 4), AQUA)   # arms
    s.add(circle(23, 61, 5.5), AQUA); s.add(circle(73, 61, 5.5), AQUA)                 # fists
    s.add(ring(23, 61, 9, 6, 2.2, -20), FOAM); s.add(ring(73, 61, 9, 6, 2.2, 20), FOAM)
    s.add(circle(48, 33, 12), AQUA)                                                   # head
    for i, (x, y) in enumerate([(40, 24), (47, 21), (54, 23)]):                      # swept wave crest
        s.add(crescent(x + 6, y - 2, 7, -3, 3, 6), MOCHI)
    if back:
        s.paint(wave_band(52, 1.5, 2.5, 2), AQUA.light, clip=True)
        s.paint(rect(44, 62, 52, 67), FOAM.base)
        return
    s.paint(rect(39, 31, 57, 34), SASH.base)                                          # headband
    eye(s, 43, 36, 1.8, 2.4); eye(s, 53, 36, 1.8, 2.4); mouth(s, 48, 41, 4)
    s.paint(ellipse(48, 55, 6, 4), AQUA.light)

def aquari_os(s, back):
    # floating fluid intelligence: water orb with a circuit-brain, fin wings, liquid tail
    s.add(chain([(48, 66), (52, 74), (46, 82), (50, 90)], 7, 1.5), DEEPBLU)
    s.add(poly([(28, 40), (6, 28), (12, 46), (4, 58), (28, 54)]), MOCHI)               # fin wings
    s.add(poly([(68, 40), (90, 28), (84, 46), (92, 58), (68, 54)]), MOCHI)
    s.paint(line(10, 36, 26, 44, 1), MOCHI.light); s.paint(line(10, 52, 26, 50, 1), MOCHI.light)
    s.paint(line(86, 36, 70, 44, 1), MOCHI.light); s.paint(line(86, 52, 70, 50, 1), MOCHI.light)
    s.add(circle(48, 44, 24), DEEPBLU)
    s.add(ellipse(48, 36, 17, 12), AQUA)                                             # brain dome
    for y0, ph in ((32, 0), (37, 1.7)):
        s.paint(wave_band(y0, 1.5, 2.2, 1.0, ph) & ellipse(48, 36, 15, 10), AQUA.outline)
    s.paint(line(48, 25, 48, 47, 1) & ellipse(48, 36, 17, 12), AQUA.outline)
    for a in range(0, 360, 60):                                                      # orbiting droplets
        import math
        x = 48 + 34 * math.cos(math.radians(a + 15)); y = 46 + 12 * math.sin(math.radians(a + 15))
        if y > 50 or a in (0, 180):
            s.add(circle(x, y, 2.2), FOAM)
    if back:
        s.paint(ring(48, 44, 20, 20, 1.2) & ~ellipse(48, 36, 18, 13), DEEPBLU.light)
        return
    s.add(rect(30, 50, 66, 56) & circle(48, 44, 23), SASH)                           # visor band
    glow_eye(s, 38, 52, 6, CYANGLW); glow_eye(s, 52, 52, 6, CYANGLW)

# ---------------------------------------------------------------- CHROME croc line
def razorgater(s, back):
    # small, low quadruped croc; flat chrome scales, teal belly, row of razor plates
    s.add(chain([(24, 74), (14, 70), (6, 62)], 6, 2), CHROME)                         # tail
    s.add(capsule(30, 78, 28, 86, 4), CHROME); s.add(capsule(46, 78, 46, 86, 4), CHROME)
    s.add(ellipse(38, 72, 17, 10), CHROME)
    s.add(capsule(36, 80, 34, 88, 4), CHROME); s.add(capsule(52, 79, 54, 88, 4), CHROME)
    spikes(s, [(26, 64), (32, 62), (38, 62), (44, 63)], BRIGHTCH, h=6, w=5, up=(-.3, -1))
    s.add(ellipse(60, 68, 12, 9), CHROME)                                             # head
    s.add(poly([(62, 66), (90, 70), (88, 76), (62, 78)]), CHROME)                     # long flat snout
    s.add(ellipse(60, 61, 5, 3), BRIGHTCH)                                            # brow ridge
    if back:
        for x in (30, 38, 46): s.paint(rect(x - 2, 68, x + 2, 70), CHROME.light)
        return
    s.paint(ellipse(42, 78, 12, 3), TEAL.base)
    s.paint(rect(64, 73, 89, 74), CHROME.outline)
    fangs(s, 72, 74, 3, 6)
    eye(s, 61, 64, 2, 2, col=TEAL.outline)
    s.paint(rect(60, 63, 62, 64), CYANGLW)
    s.paint(rect(86, 71, 88, 72), CHROME.outline)

def chromedile(s, back):
    # bipedal chrome croc, black umbral undersides & stripes, jaw-helmet, bladed tail
    s.add(chain([(56, 74), (70, 80), (84, 78), (90, 70)], 6, 2), BRIGHTCH)
    s.add(poly([(86, 72), (94, 62), (90, 76)]), VIOLET)
    s.add(capsule(42, 68, 38, 86, 6), BRIGHTCH); s.add(capsule(56, 68, 60, 86, 6), BRIGHTCH)
    s.add(ellipse(36, 88, 7, 3), VOID); s.add(ellipse(62, 88, 7, 3), VOID)
    s.add(ellipse(49, 58, 14, 17), BRIGHTCH)
    s.add(capsule(38, 50, 28, 64, 4), BRIGHTCH); s.add(capsule(60, 50, 70, 64, 4), BRIGHTCH)
    for x in (27, 71): s.add(poly([(x - 3, 64), (x + 3, 64), (x, 70)]), VOID)
    s.add(ellipse(46, 30, 12, 10), BRIGHTCH)                                          # skull
    s.add(poly([(36, 30), (14, 34), (16, 42), (40, 42)]), BRIGHTCH)                    # snout (to left)
    spikes(s, [(42, 22), (48, 21), (54, 22)], VIOLET, h=5, w=4, up=(.3, -1))
    spikes(s, [(48, 42), (52, 48), (55, 56)], VIOLET, h=5, w=4, up=(1, -.2))
    if back:
        for y in (50, 58, 66): s.paint(rect(42, y, 56, y + 2), VOID.base)
        return
    s.add(ellipse(49, 62, 8, 11), VOID)                                               # dark belly plates
    for y in (56, 62, 68): s.paint(rect(43, y, 55, y + 1), VOID.light)
    s.paint(rect(15, 38, 39, 39), BRIGHTCH.outline); fangs(s, 24, 39, 3, 5)
    glow_eye(s, 41, 28, 5, CYANGLW)

def reaperdile(s, back):
    # walking tank: hunched gunmetal hulk, tread-like leg plates, scythe forearm blades
    s.add(chain([(66, 74), (80, 82), (92, 80)], 9, 3), GUNMET)
    s.add(rect(26, 70, 42, 92) & ellipse(34, 80, 10, 14), GUNMET); s.add(rect(54, 70, 70, 92) & ellipse(62, 80, 10, 14), GUNMET)
    for y in (74, 80, 86):
        s.paint(rect(26, y, 42, y + 1), GUNMET.outline); s.paint(rect(54, y, 70, y + 1), GUNMET.outline)
    s.add(ellipse(48, 56, 24, 22), GUNMET)
    s.add(ellipse(48, 62, 14, 14), UNDERGR)
    spikes(s, [(30, 38), (40, 34), (52, 34), (62, 38)], GUNMET, h=10, w=7)
    s.add(capsule(28, 48, 14, 62, 6), GUNMET); s.add(capsule(68, 48, 82, 62, 6), GUNMET)
    s.add(crescent(10, 52, 14, 5, -4, 12) & rect(0, 30, 20, 70), CHROME)               # scythes
    s.add(crescent(86, 52, 14, -5, -4, 12) & rect(76, 30, 96, 70), CHROME)
    s.add(ellipse(48, 28, 14, 11), GUNMET)
    s.add(poly([(36, 30), (22, 34), (24, 42), (40, 40)]), GUNMET)
    s.add(poly([(60, 30), (74, 34), (72, 42), (56, 40)]), GUNMET)
    if back:
        for x in (36, 48, 60): s.paint(rect(x - 3, 46, x + 3, 70), GUNMET.light)
        s.paint(rect(44, 40, 52, 76), UNDERGR.base)
        return
    for y in (54, 60, 66, 72): s.paint(rect(38, y, 58, y + 1), UNDERGR.outline)
    s.paint(rect(24, 39, 72, 40), GUNMET.outline); fangs(s, 48, 40, 5, 5)
    glow_eye(s, 40, 26, 5, '#7dff9a'); glow_eye(s, 52, 26, 5, '#7dff9a')

# ---------------------------------------------------------------- CORE dino line
def tyrage(s, back):
    # tiny packed-earth dino; glowing green cracks; no horn
    s.add(chain([(56, 78), (66, 82), (74, 80)], 6, 2), EARTH)
    s.add(capsule(42, 76, 40, 86, 5), EARTH); s.add(capsule(54, 76, 56, 86, 5), EARTH)
    s.add(ellipse(48, 72, 13, 12), EARTH)
    s.add(capsule(38, 68, 34, 74, 2.5), EARTH); s.add(capsule(58, 68, 62, 74, 2.5), EARTH)
    s.add(ellipse(48, 52, 15, 13), EARTH)
    crack = line(40, 46, 44, 52, 1) | line(44, 52, 42, 58, 1) | line(54, 66, 58, 72, 1) | line(58, 72, 55, 78, 1) | line(44, 70, 40, 76, 1)
    s.paint(crack, '#81c784')
    s.paint(rect(38, 84, 60, 85) & ~rect(46, 84, 52, 85), '#81c784')
    for (x, y, r) in ((40, 40, 3.5), (48, 38, 4), (56, 40, 3.5), (62, 50, 3), (64, 60, 3)):
        s.add(rect(x - r, y - r * .8, x + r, y + r * .8), STONE)
    dots(s, [(42, 74), (55, 68), (50, 80), (36, 56)], 1, EARTH.shadow)
    if back:
        s.paint(line(48, 42, 50, 70, 1), '#81c784'); return
    eyes(s, 48, 51, 6, rx=2.4, ry=3)
    s.paint(rect(43, 58, 54, 59), EARTH.outline); fangs(s, 48, 59, 2, 6)

def duneclaw(s, back):
    # desert raptor-quadruped, umbral stripes, bone visor mask over the eyes only
    s.add(chain([(64, 66), (78, 60), (90, 52)], 6, 1.5), SAND)
    s.add(capsule(62, 70, 66, 88, 4), SAND); s.add(capsule(36, 70, 34, 88, 4), SAND)
    s.add(ellipse(52, 64, 18, 11), SAND)
    s.add(capsule(56, 72, 58, 88, 4), SAND); s.add(capsule(42, 72, 40, 88, 4), SAND)
    for x in (34, 40, 58, 64): s.add(poly([(x - 3, 88), (x + 3, 88), (x - 4, 91)]), BONE)
    for x in (48, 55, 62): s.paint(poly([(x, 54), (x + 3, 54), (x + 1, 66)]), UMBRAL.base)
    s.add(capsule(38, 58, 26, 46, 6), SAND)                                            # neck
    s.add(ellipse(22, 42, 10, 8), SAND)
    s.add(poly([(16, 40), (4, 44), (6, 50), (18, 48)]), SAND)
    s.add(poly([(14, 36), (30, 34), (30, 42), (14, 44)]), BONE)                        # bone visor
    if back:
        s.paint(line(30, 48, 66, 58, 1.5), UMBRAL.base); return
    glow_eye(s, 18, 39, 4, '#b39ddb'); glow_eye(s, 24, 39, 3, '#b39ddb')
    s.paint(rect(5, 47, 18, 48), SAND.outline); fangs(s, 10, 48, 2, 4)

def oblivirex(s, back):
    # black-bone tyrant: void body, exposed fossil ribs, violet ghost aura
    s.add(chain([(62, 70), (76, 76), (88, 74), (94, 66)], 10, 2), VOID)
    s.add(capsule(38, 66, 34, 90, 7), VOID); s.add(capsule(58, 66, 62, 90, 7), VOID)
    for x in (34, 62): s.add(poly([(x - 7, 90), (x + 7, 90), (x - 9, 93), (x + 9, 93)]) | rect(x - 8, 89, x + 8, 93), BONE)
    s.add(ellipse(48, 56, 18, 20), VOID)
    s.add(capsule(36, 52, 28, 60, 3), VOID); s.add(capsule(60, 52, 66, 60, 3), VOID)
    s.add(ellipse(42, 24, 16, 12), VOID)
    s.add(poly([(28, 22), (8, 26), (8, 34), (30, 36)]), VOID)
    s.add(poly([(10, 36), (30, 36), (30, 40), (12, 40)]), BONE)                        # bone jaw
    spikes(s, [(46, 13), (54, 15), (60, 20)], BONE, h=6, w=4, up=(.4, -1))
    if back:
        s.paint(line(50, 36, 56, 76, 2), BONE.base)
        for y in (44, 52, 60): s.paint(line(42, y, 62, y + 2, 1), BONE.shadow)
        return
    for y in (46, 52, 58, 64): s.paint(capsule(38, y, 58, y, 1.2) & ellipse(48, 56, 15, 17), BONE.base)
    s.paint(rect(47, 42, 49, 68), BONE.light)
    glow_eye(s, 38, 21, 5, '#b26cff'); fangs(s, 18, 36, 4, 4)

# ---------------------------------------------------------------- BEAST / FLAME cat line
def kittember(s, back):
    # sitting lavender cat; ember-tipped ears & tail; violet back stripes
    s.add(chain([(60, 82), (72, 78), (76, 66), (72, 58)], 3.5, 2.5), LAV)
    s.add(poly([(68, 58), (76, 56), (74, 46), (70, 52), (66, 48)]), EMBER)             # ember tail tip
    s.add(ellipse(48, 74, 14, 14), LAV)
    s.add(capsule(42, 76, 41, 88, 3.5), LAV); s.add(capsule(54, 76, 55, 88, 3.5), LAV)
    s.add(ellipse(48, 52, 15, 12), LAV)
    for sx in (-1, 1):
        s.add(poly([(48 + sx * 6, 44), (48 + sx * 15, 44), (48 + sx * 14, 30)]), LAV)
        s.paint(poly([(48 + sx * 11.5, 36), (48 + sx * 14, 35), (48 + sx * 14, 30)]), EMBER.base, clip=False)
    if back:
        for y in (62, 68, 74): s.paint(capsule(40, y, 56, y, 1.2), LAV.shadow)
        return
    eye(s, 42, 52, 2.2, 3, col='#ff9a2e'); eye(s, 54, 52, 2.2, 3, col='#ff9a2e')
    s.paint(rect(42, 51, 43, 54), EYE); s.paint(rect(54, 51, 55, 54), EYE)
    s.paint(rect(47, 57, 50, 58), LAV.outline)
    s.paint(ellipse(48, 76, 7, 8), LAV.hi)
    for sx in (-1, 1): s.paint(line(48 + sx * 8, 58, 48 + sx * 16, 57, 1), LAV.light)

def pyropaw(s, back):
    # standing tiger cub; lavender with flame-shaped ember stripes; flaming tail
    s.add(chain([(70, 66), (82, 58), (86, 48)], 4, 3), LAV)
    s.add(poly([(80, 50), (90, 44), (88, 32), (84, 40), (80, 36)]), EMBER)
    s.add(capsule(66, 70, 68, 88, 5), LAV); s.add(capsule(38, 70, 36, 88, 5), LAV)
    s.add(ellipse(54, 66, 20, 12), LAV)
    s.add(capsule(60, 72, 61, 88, 5), LAV); s.add(capsule(44, 72, 43, 88, 5), LAV)
    for x in (50, 58, 66): s.paint(poly([(x, 55), (x + 4, 55), (x + 1, 66), (x + 4, 62)]), EMBER.base)
    s.add(ellipse(32, 52, 15, 13), LAV)
    for sx, x0 in ((-1, 24), (1, 40)):
        s.add(poly([(x0 - 6, 44), (x0 + 6, 44), (x0 + sx * 2, 30)]), LAV)
        s.paint(poly([(x0 + sx * 2 - 2, 34), (x0 + sx * 2 + 2, 34), (x0 + sx * 2, 30)]), EMBER.base, clip=False)
    if back:
        s.paint(poly([(26, 44), (30, 44), (28, 52)]), EMBER.base); return
    eye(s, 26, 51, 2, 2.8, col='#ff9a2e'); eye(s, 38, 51, 2, 2.8, col='#ff9a2e')
    s.paint(rect(26, 50, 27, 53), EYE); s.paint(rect(38, 50, 39, 53), EYE)
    s.paint(ellipse(32, 59, 6, 4), LAV.hi); s.paint(rect(31, 57, 34, 58), LAV.outline)
    s.paint(poly([(30, 40), (34, 40), (32, 46)]), EMBER.base)

def manticlaw(s, back):
    # manticore: lion body, blazing mane, violet bat wings, ember scorpion tail
    s.add(poly([(52, 50), (66, 18), (80, 14), (94, 26), (86, 34), (90, 44), (70, 52)]), UMBRAL)   # wing (rear)
    s.add(chain([(70, 64), (84, 60), (92, 46), (88, 34)], 5, 3), LAV)
    s.add(poly([(84, 36), (92, 30), (90, 22), (86, 28)]), EMBER)
    s.add(capsule(68, 68, 70, 90, 6), LAV); s.add(capsule(36, 68, 34, 90, 6), LAV)
    s.add(ellipse(54, 64, 24, 14), LAV)
    s.add(capsule(62, 70, 63, 90, 6), LAV); s.add(capsule(44, 70, 43, 90, 6), LAV)
    for x in (52, 60, 68): s.paint(poly([(x, 52), (x + 4, 52), (x + 1, 64)]), UMBRAL.base)
    s.add(poly([(14, 30), (22, 18), (32, 22), (40, 16), (48, 26), (52, 40), (46, 64), (36, 60), (28, 66), (20, 58), (12, 60), (14, 46), (8, 40)]), FLAME)  # mane
    s.add(poly([(40, 44), (50, 14), (60, 10), (66, 20), (58, 28), (62, 36), (52, 46)]), UMBRAL)   # wing (front)
    s.add(ellipse(30, 44, 11, 11), LAV)
    s.add(poly([(22, 34), (26, 26), (30, 34)]), LAV); s.add(poly([(32, 34), (36, 26), (38, 34)]), LAV)
    if back:
        s.paint(line(50, 18, 58, 40, 1), UMBRAL.light); return
    eye(s, 25, 43, 2, 2.6, col='#ff9a2e'); eye(s, 35, 43, 2, 2.6, col='#ff9a2e')
    s.paint(ellipse(30, 50, 5, 3), LAV.hi); s.paint(rect(26, 52, 34, 53), LAV.outline); fangs(s, 30, 53, 2, 4)

# ---------------------------------------------------------------- BEAST / EARTH dog line
def pupbble(s, back):
    s.add(chain([(60, 76), (68, 70)], 3, 2), PEACH)
    s.add(ellipse(50, 76, 14, 11), PEACH)
    s.add(capsule(42, 80, 41, 88, 3.5), PEACH); s.add(capsule(56, 80, 57, 88, 3.5), PEACH)
    for (x, y, r) in ((46, 66, 4), (54, 65, 4.5), (60, 70, 3.5)): s.add(circle(x, y, r), STONE)  # pebble coat
    s.add(ellipse(42, 54, 13, 11), PEACH)
    s.add(ellipse(30, 56, 4, 8, 20), PEACH.__class__('#4a2a10', '#9a6030', '#c2884a', '#e0a868'))
    s.add(ellipse(54, 56, 4, 8, -20), PEACH.__class__('#4a2a10', '#9a6030', '#c2884a', '#e0a868'))
    s.add(circle(42, 45, 3.2), STONE)
    if back:
        return
    eyes(s, 42, 54, 5, rx=2, ry=2.6)
    s.paint(ellipse(42, 60, 4, 2.4), PEACH.hi); s.paint(rect(41, 59, 44, 60), PEACH.outline)

def terradog(s, back):
    s.add(chain([(70, 62), (80, 54), (84, 46)], 3, 2), TAN)
    s.add(capsule(66, 68, 68, 88, 4.5), TAN); s.add(capsule(40, 68, 38, 88, 4.5), TAN)
    s.add(ellipse(54, 64, 19, 11), TAN)
    s.add(capsule(60, 70, 61, 88, 4.5), TAN); s.add(capsule(46, 70, 45, 88, 4.5), TAN)
    s.add(poly([(40, 56), (54, 50), (70, 54), (72, 62), (40, 62)]), STONE)               # rock saddle
    s.add(poly([(28, 56), (38, 54), (40, 66), (30, 66)]), STONE)                         # shoulder plate
    s.paint(line(50, 54, 52, 60, 1) | line(62, 53, 60, 60, 1), STONE.outline)
    s.add(ellipse(30, 46, 12, 10), TAN)
    s.add(poly([(20, 44), (8, 48), (10, 54), (22, 52)]), TAN)
    s.add(poly([(28, 38), (34, 26), (38, 38)]), TAN); s.add(poly([(20, 38), (22, 28), (28, 37)]), TAN)
    if back: return
    eye(s, 26, 44, 1.8, 2.4); eye(s, 34, 44, 1.8, 2.4)
    s.paint(ellipse(9, 49, 2, 1.5), EYE); s.paint(rect(10, 53, 22, 54), TAN.outline)

def quakehound(s, back):
    s.add(chain([(78, 58), (88, 50)], 4, 3), PEACH.__class__('#40240c', '#8a5a2a', '#c2884a', '#e0a868'))
    TANK = R('#40240c', '#8a5a2a', '#c2884a', '#e0a868')
    s.add(capsule(72, 62, 74, 90, 7), TANK); s.add(capsule(30, 62, 28, 90, 7), TANK)
    s.add(ellipse(52, 58, 28, 17), TANK)
    s.add(capsule(64, 66, 64, 90, 7), TANK); s.add(capsule(40, 66, 39, 90, 7), TANK)
    for x in (28, 39, 64, 74): s.add(rect(x - 7, 86, x + 8, 92) & ellipse(x, 90, 8, 5), DKSTONE)
    spikes(s, [(36, 42), (46, 40), (56, 40), (66, 42), (76, 46)], DKSTONE, h=11, w=8)
    s.add(ellipse(24, 46, 16, 14), TANK)
    s.add(poly([(12, 46), (2, 52), (4, 62), (16, 60)]), TANK)
    s.add(ellipse(24, 34, 10, 4), DKSTONE)                                             # stone brow
    if back:
        s.paint(line(36, 50, 76, 52, 2), DKSTONE.base); return
    glow_eye(s, 18, 39, 4, '#ffcc80'); glow_eye(s, 28, 39, 4, '#ffcc80')
    s.paint(rect(4, 58, 16, 59), TANK.outline); fangs(s, 9, 59, 3, 4)
    s.paint(ellipse(4, 54, 2, 1.6), EYE)

# ---------------------------------------------------------------- BUG / SILK line
def squirmite(s, back):
    segs = [(66, 84, 6), (58, 82, 7), (49, 80, 8), (40, 76, 8.5), (33, 68, 9)]
    for i, (x, y, r) in enumerate(segs):
        s.add(circle(x, y, r), SILK)
        if i < 4: s.add(ellipse(x, y + r - 1, 2, 2), LIME)
    for (x, y, r) in segs[:4]: s.paint(rect(int(x) - 1, int(y - r * .5), int(x) + 1, int(y - r * .5) + 2), TEAL.base)
    s.add(capsule(29, 60, 25, 54, 1.6), SILK); s.add(capsule(37, 60, 40, 54, 1.6), SILK)
    if back: return
    eyes(s, 33, 68, 4, rx=1.8, ry=2.4)
    s.paint(rect(32, 73, 35, 74), SILK.outline)

def cocoonode(s, back):
    s.paint(line(48, 0, 48, 20, 1), SILK.base, clip=False)
    hexa = poly([(48, 18), (66, 30), (66, 70), (48, 86), (30, 70), (30, 30)])
    s.add(hexa, LIME)
    for y in (34, 44, 54, 64): s.paint(wave_band(y, 1.2, 4, 1, y * .3) & hexa, LIME.shadow)
    circ = line(38, 40, 38, 60, 1) | line(38, 60, 48, 66, 1) | line(58, 36, 58, 52, 1) | line(48, 30, 58, 36, 1)
    s.paint(circ & hexa, '#118a76')
    dots(s, [(38, 40), (48, 66), (58, 52), (48, 30)], 1.6, CYANGLW)
    if back: return
    s.add(rect(36, 46, 60, 52) & hexa, R('#111a0a', '#1e2c10', '#2a3a14', '#3a4f1e'))
    glow_eye(s, 41, 48, 3, CYANGLW); glow_eye(s, 52, 48, 3, CYANGLW)

def mothrix(s, back):
    MAT = R('#020604', '#0a1a10', '#141420', '#22303a')
    for sx in (-1, 1):
        up = poly([(48, 44), (48 + sx * 44, 10), (48 + sx * 46, 34), (48 + sx * 10, 52)])
        lo = poly([(48, 52), (48 + sx * 36, 58), (48 + sx * 28, 84), (48 + sx * 8, 66)])
        s.add(up, MAT); s.add(lo, MAT)
        grid = np.zeros((H, W), bool)
        for g in range(6, 96, 6): grid |= rect(g, 0, g + 1, 96) | rect(0, g, 96, g + 1)
        s.paint(grid & (up | lo), '#0f7a3a')
        s.paint(circle(48 + sx * 30, 26, 4) | circle(48 + sx * 22, 66, 3), NEONGRN)
    s.add(ellipse(48, 58, 6, 18), SILK)
    s.add(circle(48, 38, 7), SILK)
    for sx in (-1, 1):
        s.paint(line(48 + sx * 3, 32, 48 + sx * 14, 16, 1), SILK.shadow, clip=False)
        for t in range(3): s.paint(line(48 + sx * (6 + t * 3), 27 - t * 4, 48 + sx * (9 + t * 3), 28 - t * 4, 1), SILK.shadow, clip=False)
    if back:
        for y in (52, 58, 64): s.paint(rect(43, y, 53, y + 1), SILK.shadow); return
    glow_eye(s, 43, 37, 3, NEONGRN); glow_eye(s, 51, 37, 3, NEONGRN)

# ---------------------------------------------------------------- AERO bird line
def zephling(s, back):
    s.add(poly([(40, 84), (44, 84), (42, 89)]), STONE); s.add(poly([(52, 84), (56, 84), (54, 89)]), STONE)
    s.add(circle(48, 70, 15), SKY)
    s.add(poly([(34, 66), (24, 74), (36, 78)]), SKY); s.add(poly([(62, 66), (72, 74), (60, 78)]), SKY)
    s.add(crescent(52, 50, 8, -4, 3, 6.5), FALCON)                                    # swirl crest
    if back:
        s.paint(wave_band(66, 1.5, 3, 1.4), SKY.shadow); return
    s.paint(ellipse(48, 76, 9, 7), WHITE.base)
    eyes(s, 48, 66, 6, rx=2, ry=2.6)
    s.add(poly([(45, 70), (51, 70), (48, 75)]), STONE)

def aerobeak(s, back):
    s.add(poly([(52, 70), (80, 82), (70, 86), (50, 80)]), FALCON)                      # tail
    s.add(poly([(42, 86), (46, 86), (44, 90)]), STONE); s.add(poly([(52, 86), (56, 86), (54, 90)]), STONE)
    s.add(ellipse(48, 64, 13, 20, 15), FALCON)
    s.add(poly([(54, 50), (88, 40), (84, 48), (90, 52), (60, 72)]), FALCON)           # swept wing
    for i in range(3): s.paint(line(64 + i * 6, 48 - i, 72 + i * 6, 54 - i, 1), FALCON.light)
    s.add(ellipse(40, 38, 10, 9), FALCON)
    s.add(poly([(32, 36), (20, 40), (32, 42)]), YELLOW)
    if back:
        s.paint(line(44, 50, 52, 76, 1.5), FALCON.shadow); return
    s.paint(ellipse(42, 66, 7, 12, 15), WHITE.base)
    s.paint(poly([(30, 36), (44, 32), (48, 40), (34, 42)]), WHITE.base)                # face mask
    eye(s, 38, 37, 1.8, 2.2)
    s.paint(line(36, 34, 42, 33, 1), STORM.outline)

def stormtalon(s, back):
    for sx in (-1, 1):
        w = poly([(48 + sx * 8, 40), (48 + sx * 46, 8), (48 + sx * 44, 22), (48 + sx * 48, 30), (48 + sx * 40, 36), (48 + sx * 44, 46), (48 + sx * 14, 56)])
        s.add(w, STORM)
        s.paint(poly([(48 + sx * 36, 16), (48 + sx * 30, 26), (48 + sx * 36, 26), (48 + sx * 28, 38), (48 + sx * 40, 24), (48 + sx * 34, 24), (48 + sx * 40, 16)]), NEONYEL)
    s.add(poly([(40, 70), (56, 70), (60, 86), (48, 82), (36, 86)]), STORM)
    s.add(ellipse(48, 56, 12, 18), STORM)
    for x in (42, 54):
        s.add(capsule(x, 70, x, 82, 3), STORM)
        s.add(poly([(x - 5, 82), (x + 5, 82), (x + 4, 90), (x, 86), (x - 4, 90)]), YELLOW)
    s.add(ellipse(48, 32, 10, 9), STORM)
    s.add(poly([(42, 30), (56, 22), (60, 26), (52, 32)]), STORM)                        # crest
    s.add(poly([(44, 36), (52, 36), (48, 44)]), YELLOW)
    if back:
        s.paint(line(48, 40, 48, 70, 1.5), STORM.light); return
    s.paint(ellipse(48, 60, 6, 10), SKY.base)
    glow_eye(s, 41, 31, 4, NEONYEL); glow_eye(s, 51, 31, 4, NEONYEL)

# ---------------------------------------------------------------- AQUA / CHROME fish
def finblade(s, back):
    s.add(poly([(70, 60), (88, 46), (84, 62), (88, 76)]), AQUA)                       # tail
    s.add(poly([(44, 52), (54, 36), (62, 52)]), AQUA)                                  # dorsal
    s.add(ellipse(50, 62, 22, 10), BRIGHTCH)
    s.add(poly([(30, 60), (2, 62), (30, 64)]), BRIGHTCH)                               # sword
    s.add(poly([(46, 68), (40, 80), (54, 70)]), AQUA)
    s.paint(line(62, 56, 62, 68, 1) | line(66, 57, 66, 67, 1), CHROME.shadow)
    if back:
        s.paint(rect(32, 56, 70, 58) & ellipse(50, 62, 22, 10), AQUA.base); return
    s.paint(ellipse(50, 66, 18, 4), WHITE.base)
    eye(s, 36, 60, 2, 2.2, white=True)

def megalochrome(s, back):
    s.add(poly([(70, 54), (94, 30), (90, 54), (94, 78)]), CHROME)
    s.add(poly([(36, 40), (50, 14), (60, 40)]), CHROME)
    s.add(ellipse(46, 54, 40, 18), CHROME)
    s.add(poly([(34, 64), (22, 86), (46, 68)]), CHROME); s.add(poly([(56, 66), (62, 80), (66, 64)]), CHROME)
    for x in (24, 40, 56, 70): s.paint(circle(x, 46, 1), CHROME.light)
    if back:
        for x in (24, 40, 56): s.paint(rect(x, 40, x + 2, 64), CHROME.shadow); return
    s.paint(ellipse(40, 62, 30, 7), BRIGHTCH.base)
    s.add(poly([(8, 56), (30, 54), (32, 64), (12, 64)]), R('#0a0a10', '#18181f', '#2a0f18', '#3a1420'))
    fangs(s, 18, 56, 4, 4); s.paint(poly([(12, 64), (30, 64), (20, 61)]), '#ffffff')
    for x in (40, 45, 50): s.paint(line(x, 50, x - 2, 58, 1), TEAL.base)
    glow_eye(s, 24, 48, 4, CYANGLW)

def floatcalf(s, back):
    s.add(poly([(64, 60), (82, 52), (78, 62), (82, 70)]), NAVY)
    s.add(ellipse(46, 62, 22, 16), NAVY)
    s.add(ellipse(42, 78, 6, 3, -20), NAVY)
    for x, y, c in ((30, 54, HOTPINK), (44, 50, NEONYEL), (56, 56, HOTPINK), (50, 66, NEONYEL), (62, 64, HOTPINK)):
        s.paint(circle(x, y, 2.2), c)
    s.add(circle(40, 40, 3), FOAM); s.add(circle(46, 34, 2), FOAM); s.add(circle(43, 28, 1.5), FOAM)
    if back: return
    s.paint(ellipse(42, 72, 16, 5), NAVY.light)
    eye(s, 30, 62, 2, 2.6, white=True); s.paint(rect(24, 70, 34, 71), NAVY.outline)

def astroleviathan(s, back):
    s.add(poly([(74, 44), (96, 22), (92, 46), (96, 70)]), INDIGO)
    s.add(ellipse(44, 50, 42, 24), INDIGO)
    s.add(poly([(34, 70), (20, 92), (50, 72)]), INDIGO)
    s.add(ring(48, 50, 46, 10, 2, -12), NEONPK)                                       # neon orbit ring
    import random
    rnd = random.Random(25)
    for _ in range(26):
        x, y = rnd.randint(8, 82), rnd.randint(30, 70)
        s.paint(rect(x, y, x + 1, y + 1), rnd.choice(['#ffffff', NEONYEL, '#b0b8ff']))
    for x, y in ((28, 40), (52, 36), (64, 50)): s.paint(circle(x, y, 2), NEONYEL)
    if back: return
    s.paint(ellipse(36, 62, 30, 8) & ellipse(44, 50, 41, 23), INDIGO.light)
    for x in range(14, 60, 6): s.paint(rect(x, 60, x + 1, 68) & ellipse(36, 62, 30, 8), INDIGO.shadow)
    glow_eye(s, 14, 46, 5, HOTPINK)

# ---------------------------------------------------------------- AQUA / UMBRAL cephalopods
def inklet(s, back):
    for i, x in enumerate((38, 45, 52, 59)):
        s.add(chain([(x, 70), (x - 2 + (i % 2) * 4, 80), (x + (i % 2) * 2 - 1, 88)], 3, 1.2), INK)
    drop = circle(48, 64, 14) | poly([(36, 58), (48, 34), (60, 58)])
    s.add(drop, INK)
    s.paint(ellipse(42, 52, 3, 5, -20) & drop, INK.light)
    if back: return
    eye(s, 42, 64, 3, 3.6, col='#ffffff', glint=False); eye(s, 54, 64, 3, 3.6, col='#ffffff', glint=False)
    s.paint(rect(42, 64, 44, 67), '#80deea'); s.paint(rect(54, 64, 56, 67), '#80deea')

def toxitacle(s, back):
    for i, (x0, x1, y1) in enumerate([(34, 14, 80), (40, 28, 90), (48, 48, 92), (56, 68, 90), (62, 82, 80)]):
        s.add(chain([(x0, 64), ((x0 + x1) / 2 + (6 if i % 2 else -6), (64 + y1) / 2), (x1, y1)], 4, 1.5), TOXIC)
        s.paint(circle((x0 + x1) / 2 + (6 if i % 2 else -6), (64 + y1) / 2 + 2, 1.2), NEONGRN)
    s.add(ellipse(48, 46, 18, 22), TOXIC)
    s.paint(circle(40, 30, 3) | circle(57, 28, 2) | circle(50, 35, 2.2), NEONGRN)
    if back: return
    s.add(ellipse(48, 47, 13, 5), INK)
    glow_eye(s, 39, 46, 5, NEONGRN); glow_eye(s, 52, 46, 5, NEONGRN)
    s.paint(ellipse(48, 60, 3, 2), INK.base)
    s.paint(line(44, 70, 44, 76, 1), NEONGRN, clip=False)

def krakenox(s, back):
    import math
    for i in range(8):
        a = math.radians(200 + i * 20)
        x0, y0 = 48 + 14 * math.cos(a), 52
        pts = [(x0, y0)]
        for t in range(1, 5):
            r = 8 * t
            pts.append((x0 + math.cos(a) * r * 1.2 + (4 if i % 2 else -4) * math.sin(t), y0 + r * .9 + (t > 2) * 4))
        s.add(chain(pts, 6, 1.8), NAVY)
        s.paint(circle(pts[2][0], pts[2][1] + 2, 1.4), CYANGLW)
    s.add(ellipse(48, 34, 24, 28), NAVY)
    s.add(poly([(40, 8), (48, -2), (56, 8)]), NAVY)
    if back:
        for y in (20, 30, 40): s.paint(wave_band(y, 1.5, 3, 1), NAVY.light); return
    s.add(ellipse(48, 46, 18, 8), INDIGO)
    glow_eye(s, 34, 42, 7, CYANGLW); glow_eye(s, 55, 42, 7, CYANGLW)
    s.paint(rect(36, 40, 39, 41) | rect(57, 40, 60, 41), '#ffffff')

# ---------------------------------------------------------------- CORE / STRIKE fighter line
def _fighter(s, back, scale, gloves, belt=None, kick=False, headband=True, muscle=False):
    k = scale
    cx, gy = 48, 90
    def P(x, y): return (cx + x * k, gy - y * k)
    lx, ly = P(-6, 0)
    if kick:
        s.add(capsule(*P(-4, 22), *P(-8, 2), 4.2 * k), CORAL)
        s.add(capsule(*P(4, 22), *P(26, 32), 4.2 * k), CORAL)                           # raised kick
        s.add(ring(*P(22, 30), 4.2 * k, 4.2 * k, 2 * k), gloves)
        s.add(ellipse(*P(29, 33), 4 * k, 2.6 * k, -30), CORAL)
    else:
        s.add(capsule(*P(-5, 22), *P(-8, 3), 4.2 * k), CORAL); s.add(capsule(*P(5, 22), *P(8, 3), 4.2 * k), CORAL)
        s.add(ellipse(*P(-9, 1), 5 * k, 2.4 * k), CORAL); s.add(ellipse(*P(9, 1), 5 * k, 2.4 * k), CORAL)
    s.add(rect(*P(-10, 27), *P(10, 20)), SASH if not kick else INK)                      # shorts / gi
    tw = 12 if muscle else 9
    s.add(ellipse(*P(0, 33), tw * k, 10 * k), CORAL)
    if belt: s.add(rect(*P(-11, 25), *P(11, 22)) & ellipse(*P(0, 30), (tw + 1) * k, 10 * k), belt)
    sh = tw - 1
    s.add(capsule(*P(-sh, 40), *P(-sh - 5, 32), 3.4 * k * (1.3 if muscle else 1)), CORAL)
    s.add(capsule(*P(sh, 40), *P(sh + 5, 32), 3.4 * k * (1.3 if muscle else 1)), CORAL)
    s.add(circle(*P(-sh - 6, 30), 5.2 * k), gloves); s.add(circle(*P(sh + 6, 30), 5.2 * k), gloves)
    s.add(circle(*P(0, 50), 8.5 * k), CORAL)
    s.add(ellipse(*P(-7, 55), 3 * k, 4 * k, -30), CORAL); s.add(ellipse(*P(7, 55), 3 * k, 4 * k, 30), CORAL)   # round ears
    if headband:
        s.add(rect(*P(-9, 54), *P(9, 51)) & circle(*P(0, 50), 9 * k), TEAL)
        s.add(poly([P(8, 53), P(16, 56), P(14, 50)]), TEAL)
    if back:
        s.paint(line(*P(0, 42), *P(0, 26), 1), CORAL.shadow); return
    ex, ey = P(0, 48)
    eye(s, ex - 3.4 * k, ey, 1.4 * k, 1.9 * k); eye(s, ex + 3.4 * k, ey, 1.4 * k, 1.9 * k)
    mouth(s, int(ex), int(ey + 4 * k), int(3 * k))
    if muscle: s.paint(line(*P(0, 40), *P(0, 28), 1), CORAL.shadow)

def punchkid(s, back):    _fighter(s, back, 1.05, TEAL)
def strikechamp(s, back): _fighter(s, back, 1.5, TEAL, belt=GOLD, muscle=True)
def kickmaster(s, back):  _fighter(s, back, 1.4, TEAL, belt=INK, kick=True, headband=True, muscle=True)

# ---------------------------------------------------------------- CHROME / CORE robot line
def _cog(s, cx, cy, r, ramp, teeth=8, t=3):
    import math
    m = circle(cx, cy, r)
    for i in range(teeth):
        a = math.radians(i * 360 / teeth)
        m |= capsule(cx, cy, cx + math.cos(a) * (r + t), cy + math.sin(a) * (r + t), 2)
    s.add(m, ramp)
    s.add(circle(cx, cy, r * .45), ramp)

def gearkid(s, back):
    s.add(capsule(42, 76, 41, 86, 3.4), CHROME); s.add(capsule(54, 76, 55, 86, 3.4), CHROME)
    s.add(rect(36, 84, 46, 89), GUNMET); s.add(rect(50, 84, 60, 89), GUNMET)
    s.add(rect(38, 60, 58, 78), CHROME)
    s.add(capsule(37, 64, 30, 74, 2.6), CHROME); s.add(capsule(59, 64, 66, 74, 2.6), CHROME)
    s.add(circle(29, 76, 3.2), GUNMET); s.add(circle(67, 76, 3.2), GUNMET)
    _cog(s, 48, 44, 12, CHROME, teeth=10)
    s.add(rect(40, 38, 56, 50) & circle(48, 44, 11), GUNMET)
    if back:
        _cog(s, 48, 68, 5, GUNMET, 6, 2); return
    s.paint(circle(48, 69, 3.5), '#ff9a2e')
    glow_eye(s, 42, 43, 4, '#ff9a2e'); glow_eye(s, 51, 43, 4, '#ff9a2e')

def mechapion(s, back):
    s.add(rect(30, 72, 42, 88), GUNMET); s.add(rect(54, 72, 66, 88), GUNMET)
    s.add(rect(26, 86, 44, 92), CHROME); s.add(rect(52, 86, 70, 92), CHROME)
    s.add(poly([(28, 40), (68, 40), (64, 74), (32, 74)]), CHROME)
    for x in (14, 82):                                                                   # piston arms
        s.add(rect(x - 3, 44, x + 3, 66), GUNMET)
        s.add(rect(x - 6, 36, x + 6, 48), CHROME)
        s.add(rect(x - 7, 64, x + 7, 76), CHROME)
    s.paint(rect(12, 50, 16, 52) | rect(80, 50, 84, 52), '#ff9a2e')
    s.add(rect(36, 22, 60, 40), CHROME)
    s.add(rect(46, 16, 50, 22), GUNMET); s.add(circle(48, 15, 2.5), ORANGE)
    if back:
        s.add(rect(38, 46, 58, 64), GUNMET)
        for y in (50, 56): s.paint(rect(40, y, 56, y + 2), ORANGE.base); return
    s.add(circle(48, 56, 7), GUNMET); s.paint(circle(48, 56, 4), '#ff9a2e')
    s.add(rect(39, 28, 57, 34), GUNMET); glow_eye(s, 41, 30, 5, '#ff9a2e'); glow_eye(s, 51, 30, 5, '#ff9a2e')

def gorokappa(s, back):
    s.add(capsule(30, 70, 28, 88, 7), GUNMET); s.add(capsule(66, 70, 68, 88, 7), GUNMET)
    s.add(ellipse(48, 56, 28, 22), GUNMET)
    s.add(capsule(22, 44, 10, 78, 8), GUNMET); s.add(capsule(74, 44, 86, 78, 8), GUNMET)   # long ape arms
    s.add(ellipse(8, 84, 9, 7), CHROME); s.add(ellipse(88, 84, 9, 7), CHROME)
    for x in (28, 68): s.add(rect(x - 3, 30, x + 3, 40), CHROME); s.paint(rect(x - 2, 24, x + 2, 30) & ~rect(x - 1, 27, x + 1, 28), '#d8e0e6', clip=False)  # steam vents
    s.add(ellipse(48, 32, 14, 12), GUNMET)
    s.add(ellipse(48, 21, 12, 4), CHROME)                                              # kappa plate
    s.paint(ellipse(48, 20, 8, 2), '#ff9a2e')
    if back:
        for y in (48, 56, 64): s.paint(rect(30, y, 66, y + 2), GUNMET.light); return
    s.add(ellipse(48, 62, 14, 12), CHROME)
    s.paint(circle(48, 62, 4), '#ff9a2e')
    s.add(ellipse(48, 38, 9, 5), CHROME)
    glow_eye(s, 40, 30, 5, '#ff9a2e'); glow_eye(s, 51, 30, 5, '#ff9a2e')
    s.paint(rect(43, 39, 53, 40), GUNMET.outline)

# ---------------------------------------------------------------- CORE / CHROME golem line
def pebblefist(s, back):
    s.add(capsule(43, 76, 41, 87, 3.6), STONE); s.add(capsule(53, 76, 55, 87, 3.6), STONE)
    s.add(ellipse(48, 68, 10, 10), STONE)
    s.add(capsule(40, 64, 30, 70, 2.4), STONE); s.add(capsule(56, 64, 66, 70, 2.4), STONE)
    s.add(circle(26, 72, 8), STONE); s.add(circle(70, 72, 8), STONE)                    # big stone fists
    s.add(rect(18, 68, 34, 71) & circle(26, 72, 8.5), BRIGHTCH); s.add(rect(62, 68, 78, 71) & circle(70, 72, 8.5), BRIGHTCH)
    s.add(ellipse(48, 52, 9, 8), STONE)
    s.paint(line(44, 70, 50, 74, 1), STONE.shadow)
    if back: return
    s.add(rect(40, 50, 56, 54) & ellipse(48, 52, 9, 8), TEAL)
    s.paint(rect(42, 51, 54, 53), CYANGLW)

def cragarm(s, back):
    s.add(capsule(40, 70, 36, 88, 5), STONE); s.add(capsule(56, 70, 60, 88, 5), STONE)
    s.add(poly([(34, 40), (62, 40), (60, 72), (36, 72)]), STONE)
    for (x, y) in ((22, 48), (74, 48)): s.add(circle(x, y, 7), BRIGHTCH)               # chrome shoulder joints
    s.add(poly([(10, 54), (28, 54), (32, 76), (24, 86), (8, 84), (4, 70)]), DKSTONE)    # boulder arms
    s.add(poly([(68, 54), (86, 54), (92, 70), (88, 84), (72, 86), (64, 76)]), DKSTONE)
    s.paint(line(10, 66, 20, 72, 1) | line(80, 64, 86, 74, 1), DKSTONE.outline)
    s.add(ellipse(48, 32, 10, 9), STONE)
    s.paint(line(40, 48, 46, 58, 1) | line(54, 46, 50, 62, 1), STONE.shadow)
    if back: return
    s.add(rect(39, 30, 57, 35) & ellipse(48, 32, 10, 9), BRIGHTCH); s.paint(rect(41, 31, 55, 33), CYANGLW)

def terrapod(s, back):
    s.add(rect(26, 70, 42, 92), DKSTONE); s.add(rect(54, 70, 70, 92), DKSTONE)
    s.add(poly([(20, 40), (32, 18), (40, 30), (48, 10), (56, 30), (64, 18), (76, 40), (70, 74), (26, 74)]), DKSTONE)  # mountain torso
    s.paint(poly([(30, 22), (34, 22), (32, 18)]) | poly([(46, 14), (50, 14), (48, 10)]) | poly([(62, 22), (66, 22), (64, 18)]), '#ffffff')  # snowcaps
    s.paint(rect(26, 64, 70, 66), BRIGHTCH.base)                                          # chrome band
    s.paint(line(30, 40, 34, 70, 1) & ~rect(0, 64, 96, 66), MOSS.base)
    for x in (12, 84):
        s.add(capsule(x, 44, x, 66, 7), DKSTONE)
        s.add(ellipse(x, 76, 11, 10), STONE)
        s.add(rect(x - 11, 70, x + 11, 73) & ellipse(x, 76, 11.5, 10.5), BRIGHTCH)
    if back: return
    s.add(rect(36, 40, 60, 46), BRIGHTCH); glow_eye(s, 39, 42, 6, '#81c784'); glow_eye(s, 51, 42, 6, '#81c784')

# ---------------------------------------------------------------- FLORA / CHROME turtle line
def _turtle(s, back, k, skin, shell, rim, leaves=0, bush=0, moss=0, spikesn=0, rivets=False, vines=False, crest=False):
    cx, gy = max(48, 4 + 37 * k), 90
    def P(x, y): return (cx + x * k, gy - y * k)
    for x in (-14, 14):
        s.add(rect(*P(x - 4, 8), *P(x + 4, 0)), skin)
    s.add(ellipse(*P(0, 12), 22 * k, 7 * k), rim)
    sh = ellipse(*P(0, 16), 19 * k, 15 * k) & rect(0, 0, 96, P(0, 10)[1])
    s.add(sh, shell)
    # hex plates
    import math
    for (hx, hy) in ((0, 20), (-10, 15), (10, 15)):
        x, y = P(hx, hy); r = 4.2 * k
        s.paint(poly([(x + r * math.cos(math.radians(a)), y + r * math.sin(math.radians(a))) for a in range(0, 360, 60)]) & sh & ~ellipse(x, y, r * .7, r * .7), shell.outline)
    for i in range(spikesn):
        x = -12 + i * 24 / max(1, spikesn - 1)
        s.add(poly([P(x - 2.5, 26 - abs(x) * .4), P(x + 2.5, 26 - abs(x) * .4), P(x, 33 - abs(x) * .4)]), BRIGHTCH)
    for (lx, ly, sz) in [(-6, 28, 1), (4, 30, 1.2), (12, 26, .9)][:leaves]:
        x, y = P(lx, ly)
        s.paint(line(x, y + 3 * k, x, y + 7 * k, 1), FLORA.outline, clip=False)
        s.add(rect(x - 2.5 * k * sz, y - 2.5 * k * sz, x + 2.5 * k * sz, y + 2.5 * k * sz), FLORA)
    for (bx, by, br) in [(-10, 26, 6), (2, 30, 7), (12, 25, 5.5)][:bush]:
        s.add(circle(*P(bx, by), br * k), FLORA)
    if crest:
        for x in (-9, 0, 9):
            s.add(poly([P(x - 4, 24 - abs(x) * .5), P(x + 4, 24 - abs(x) * .5), P(x + 2.5, 32 - abs(x) * .5), P(x - 2.5, 32 - abs(x) * .5)]), BRIGHTCH)
    if vines:
        for (vx, vy, sz) in [(-14, 14, 1), (-6, 26, 1.1), (5, 28, 1.2), (14, 18, 1), (-1, 33, .9)]:
            x, y = P(vx, vy)
            s.add(rect(x - 2.2 * k * sz, y - 2.2 * k * sz, x + 2.2 * k * sz, y + 2.2 * k * sz), FLORA)
        s.paint((wave_band(P(0, 14)[1], 1.5 * k, 2.2 * k, 1.2) | wave_band(P(0, 22)[1], 1.2 * k, 2.6 * k, 1.0, 1.3)) & sh, FLORA.shadow)
    for (mx, my, mr) in [(-8, 22, 6), (7, 26, 5), (12, 16, 4)][:moss]:
        s.paint(ellipse(*P(mx, my), mr * k, mr * .6 * k) & sh, MOSS.base)
    if rivets:
        for x in range(-16, 17, 6): s.paint(circle(*P(x, 11), 1), BRIGHTCH.light)
    s.add(capsule(*P(-18, 12), *P(-28, 16), 5 * k), skin)                                # neck
    s.add(ellipse(*P(-30, 18), 7 * k, 6 * k), skin)
    if back: return
    eye(s, *P(-31, 19), 1.4 * k, 1.8 * k); s.paint(rect(*P(-36, 15), *P(-29, 14.6)), skin.outline)

def sproutle(s, back):   _turtle(s, back, 1.0, MINT, CHROME, R('#1b3b2a', '#3f7a58', '#6aa886', '#a5d6a7'), leaves=3)
def shellguard(s, back): _turtle(s, back, 1.3, R('#16301f', '#3a6a4c', '#5f9a72', '#8fc7a0'), CHROME, GUNMET, vines=True, crest=True)
def dreadtoise(s, back): _turtle(s, back, 1.48, R('#122018', '#2c4a38', '#46705a', '#6f9a80'), GUNMET, R('#0e1418', '#263238', '#37474f', '#546e7a'), moss=3, spikesn=5, rivets=True)

# ---------------------------------------------------------------- singles
def pixilite(s, back):
    s.paint(line(48, 66, 48, 82, 1), FLORA.base, clip=False)
    s.add(rect(42, 74, 48, 78) | rect(48, 70, 54, 74), FLORA)
    for (dx, dy, c) in ((0, -12, NEONPK), (12, 0, YELLOW), (0, 12, NEONPK), (-12, 0, YELLOW)):
        s.add(rect(48 + dx - 6, 50 + dy - 6, 48 + dx + 6, 50 + dy + 6), c)
    s.add(rect(40, 42, 56, 58), GLITCH)
    for (x, y) in ((30, 30), (68, 34), (64, 70), (28, 66)): s.paint(rect(x, y, x + 2, y + 2), NEONGRN, clip=False)
    if back: return
    eyes(s, 48, 49, 4, rx=1.6, ry=2.2); s.paint(rect(46, 54, 50, 55), GLITCH.outline)

def wispkin(s, back):
    body = circle(48, 62, 14) | poly([(36, 58), (44, 28), (48, 40), (56, 24), (60, 58)])
    s.add(body, WISP)
    s.add(chain([(40, 72), (34, 82), (40, 88)], 4, 1.5), WISP); s.add(chain([(56, 72), (62, 80), (58, 86)], 4, 1.5), WISP)
    s.paint(ellipse(48, 62, 7, 9) | poly([(44, 56), (50, 38), (54, 56)]), WISP.hi)
    if back: return
    s.add(ellipse(48, 62, 10, 6), UMBRAL)
    glow_eye(s, 42, 61, 3, '#e9e0ff'); glow_eye(s, 51, 61, 3, '#e9e0ff')

def duskfiend(s, back):
    cloak = poly([(48, 10), (66, 26), (72, 60), (80, 92), (60, 84), (48, 92), (36, 84), (16, 92), (24, 60), (30, 26)])
    s.add(cloak, UMBRAL)
    for sx in (-1, 1):
        s.add(capsule(48 + sx * 16, 44, 48 + sx * 30, 62, 3), UMBRAL)
        for t in range(3): s.add(line(48 + sx * 30, 62, 48 + sx * (30 + t * 3), 72 + t, 1.6), VOID)
    s.add(ellipse(48, 30, 11, 13) & cloak, VOID)                                       # hood void
    if back:
        s.paint(line(48, 16, 48, 86, 1), UMBRAL.shadow); return
    s.paint(crescent(48, 36, 6, 0, -3, 6), '#3d3d55')
    glow_eye(s, 42, 27, 4, CYANGLW); glow_eye(s, 51, 27, 4, CYANGLW)

def ashemit(s, back):
    ASH = R('#2a2622', '#5a554e', '#8a857b', '#b9b3a6')
    s.add(poly([(48, 40), (64, 64), (62, 88), (34, 88), (32, 64)]), ASH)                # hooded cloak
    s.add(ellipse(48, 46, 11, 11), ASH)
    s.add(poly([(42, 38), (48, 26), (54, 38)]), ASH)
    s.add(ellipse(48, 70, 6, 4), ASH)
    s.add(poly([(44, 68), (48, 58), (52, 68)]), EMBER)                                  # cupped spark
    if back:
        s.paint(line(48, 50, 48, 86, 1), ASH.shadow); return
    s.add(ellipse(48, 48, 7, 6), VOID)
    glow_eye(s, 44, 47, 2, '#ff9a2e'); glow_eye(s, 50, 47, 2, '#ff9a2e')
    for (x, y) in ((40, 30), (58, 34), (36, 56)): s.paint(rect(x, y, x + 1, y + 1), '#b9b3a6', clip=False)

def pyromonk(s, back):
    ASH = R('#2a2622', '#5a554e', '#8a857b', '#b9b3a6')
    s.paint(line(80, 20, 70, 90, 2), RAG.shadow, clip=False)                           # staff
    s.add(poly([(76, 10), (86, 14), (84, 26), (78, 30), (74, 22)]), FLAME)              # burning head
    s.add(poly([(48, 36), (66, 52), (68, 90), (28, 90), (30, 52)]), FLAME)              # robe
    s.add(poly([(30, 52), (48, 40), (60, 66), (48, 72)]), ORANGE)                        # sash wrap
    s.add(capsule(62, 54, 74, 56, 3), FLAME); s.add(circle(75, 56, 3.4), ASH)
    s.add(capsule(34, 54, 28, 66, 3), FLAME); s.add(circle(28, 68, 3.4), ASH)
    s.add(ellipse(48, 28, 10, 10), ASH)
    for (x, y) in ((38, 70), (58, 76), (44, 84)): s.paint(circle(x, y, 1), GOLD.base)
    if back:
        s.paint(ellipse(48, 24, 8, 4), FLAME.base); return
    s.paint(rect(40, 22, 56, 24), GOLD.base)
    glow_eye(s, 43, 28, 3, '#ff9a2e'); glow_eye(s, 50, 28, 3, '#ff9a2e')
    mouth(s, 48, 33, 3)

def yogiferno(s, back):
    import math
    for i in range(9):                                                                    # lotus of flame petals
        a = math.radians(180 + i * 22.5)
        x, y = 48 + 36 * math.cos(a), 52 + 34 * math.sin(a)
        s.add(poly([(48 + 22 * math.cos(a - .25), 52 + 22 * math.sin(a - .25)), (x, y), (48 + 22 * math.cos(a + .25), 52 + 22 * math.sin(a + .25))]), EMBER)
    LAVA = R('#3a0a00', '#8a2a05', '#b8420f', '#f08030')
    s.add(ellipse(48, 78, 26, 8), LAVA)                                                   # crossed legs
    s.add(ellipse(48, 58, 14, 16), LAVA)
    s.add(capsule(36, 50, 28, 70, 3.4), LAVA); s.add(capsule(60, 50, 68, 70, 3.4), LAVA)
    s.add(circle(48, 34, 10), LAVA)
    s.paint(line(42, 60, 46, 70, 1) | line(54, 56, 50, 68, 1), '#ffc061')
    s.add(ellipse(48, 90, 20, 3), FLAME)
    if back: return
    s.paint(circle(48, 28, 1.6), GOLD.base)
    s.paint(rect(42, 34, 46, 35) | rect(50, 34, 54, 35), '#ffe08a')                     # closed eyes
    s.add(circle(48, 72, 4), GOLD)

def mythar(s, back):
    import math
    for i in range(8):
        a = math.radians(i * 45 + 22.5)
        x, y = 48 + 40 * math.cos(a), 44 + 34 * math.sin(a)
        s.add(rect(x - 2, y - 2, x + 2, y + 2), GOLD)
    for sx in (-1, 1):                                                                    # light-ribbon wings
        s.add(poly([(48 + sx * 8, 40), (48 + sx * 40, 22), (48 + sx * 32, 40), (48 + sx * 42, 56), (48 + sx * 10, 56)]), IVORY)
        s.paint(line(48 + sx * 14, 44, 48 + sx * 34, 32, 1) | line(48 + sx * 14, 50, 48 + sx * 36, 52, 1), GOLD.light)
    s.add(poly([(48, 46), (62, 66), (54, 90), (42, 90), (34, 66)]), IVORY)               # robe of light
    s.add(poly([(48, 14), (60, 34), (48, 56), (36, 34)]), GOLD)                          # diamond core
    s.add(poly([(48, 22), (54, 34), (48, 46), (42, 34)]), VIOLET)
    s.add(poly([(38, 12), (42, 4), (46, 10), (48, 2), (50, 10), (54, 4), (58, 12)]), GOLD)  # crown
    if back: return
    glow_eye(s, 44, 32, 3, '#ffffff'); glow_eye(s, 50, 32, 3, '#ffffff')

def emburrn(s, back):
    s.add(ellipse(48, 74, 22, 14), VOID)
    s.paint(line(34, 66, 40, 74, 1) | line(40, 74, 36, 82, 1) | line(58, 64, 62, 72, 1) | line(52, 78, 60, 82, 1), '#ff9a2e')
    for sx in (-1, 1):                                                                    # digging claws
        s.add(ellipse(48 + sx * 22, 82, 8, 5), EMBER)
        for t in range(3): s.add(poly([(48 + sx * (16 + t * 5), 84), (48 + sx * (19 + t * 5), 84), (48 + sx * (18 + t * 5), 90)]), BONE)
    s.add(poly([(44, 60), (48, 50), (52, 60)]), FLAME)
    if back:
        s.paint(line(44, 62, 52, 84, 1), '#ff9a2e'); return
    s.add(ellipse(48, 74, 5, 4), FLAME)                                                   # snout glow
    glow_eye(s, 38, 68, 3, '#ffc061'); glow_eye(s, 55, 68, 3, '#ffc061')

def aquabble(s, back):
    s.add(ring(48, 62, 26, 26, 2), FOAM)                                                 # bubble
    s.paint(crescent(40, 52, 8, 3, 3, 7), '#ffffff', clip=False)
    BB = R('#0e1e4a', '#3a5ab8', '#6890F0', '#a8c0ff')
    s.add(ellipse(48, 68, 13, 11), BB)
    s.add(poly([(36, 64), (28, 58), (34, 72)]), BB); s.add(poly([(60, 64), (68, 58), (62, 72)]), BB)
    s.add(poly([(44, 58), (48, 50), (52, 58)]), BB)
    if back: return
    s.paint(ellipse(48, 72, 7, 5), BB.hi)
    eyes(s, 48, 66, 5, rx=2, ry=2.6)

def _mochishape(s, ramp, back, sword=False):
    s.add(ellipse(32, 46, 6, 13, -25), ramp); s.add(ellipse(64, 46, 6, 13, 25), ramp)
    s.add(ellipse(48, 68, 19, 20), ramp)
    s.add(ellipse(40, 88, 6, 3), ramp); s.add(ellipse(56, 88, 6, 3), ramp)

def mochling(s, back):
    if not back:
        s.paint(line(72, 50, 84, 34, 2.5), '#cccc00', clip=False)
    _mochishape(s, PINK, back)
    s.add(rect(30, 60, 66, 64) & ellipse(48, 68, 19.5, 20.5), TEAL)                    # headset band
    s.add(circle(30, 62, 3.5), TEAL); s.add(circle(66, 62, 3.5), TEAL)
    if back:
        s.paint(line(70, 54, 60, 82, 2), '#cccc00', clip=False); return
    s.add(rect(68, 50, 78, 54), GUNMET)                                                  # sword guard
    eyes(s, 48, 70, 6, rx=2, ry=2.8)
    s.paint(rect(45, 77, 52, 78), PINK.outline)

def glitch_mochi(s, back):
    _mochishape(s, GLITCH, back)
    for (y0, y1, dx) in ((52, 56, 5), (70, 73, -6), (80, 82, 4)):                      # glitch slices
        s.paint(rect(30 + dx, y0, 66 + dx, y1), GLITCH.light, clip=False)
    for (x, y, c) in ((26, 60, RED), (70, 74, '#ffffff'), (62, 50, RED), (34, 82, '#141420')):
        s.paint(rect(x, y, x + 3, y + 2), c, clip=False)
    if back: return
    s.paint(rect(39, 66, 44, 70), RED); s.paint(rect(52, 66, 57, 70), '#ffffff')
    s.paint(rect(42, 76, 55, 78) & ~rect(45, 76, 47, 78) & ~rect(50, 76, 52, 78), '#141420')

def neon_stalker(s, back):
    s.add(capsule(42, 64, 36, 88, 3.4), VOID); s.add(capsule(54, 64, 62, 88, 3.4), VOID)
    s.add(poly([(48, 30), (62, 40), (58, 70), (38, 70), (34, 40)]), VOID)
    s.add(capsule(36, 42, 24, 64, 3), VOID); s.add(capsule(60, 42, 72, 64, 3), VOID)
    for x in (24, 72):
        for t in (-3, 0, 3): s.add(line(x, 64, x + t, 71, 1.3), INK)
    s.add(poly([(48, 12), (60, 26), (58, 38), (38, 38), (36, 26)]), VOID)               # hood
    s.paint(line(36, 40, 40, 70, 1) | line(60, 40, 56, 70, 1) | line(36, 64, 38, 88, 1), HOTPINK)
    s.paint(line(54, 64, 61, 88, 1), CYANGLW)
    if back:
        s.paint(line(48, 16, 48, 68, 1), HOTPINK); return
    s.paint(rect(40, 28, 56, 31), CYANGLW)

def ragdoll_brute(s, back):
    s.add(capsule(38, 72, 34, 88, 6), RAG); s.add(capsule(58, 72, 62, 88, 6), RAG)
    s.add(ellipse(48, 58, 22, 20), VIOLET)                                               # patchwork overalls
    s.add(rect(30, 44, 48, 60) & ellipse(48, 58, 22, 20), RAG)                            # patch
    s.add(capsule(28, 46, 12, 74, 7), RAG); s.add(capsule(68, 46, 84, 74, 7), VIOLET)
    s.add(circle(48, 30, 13), RAG)
    stitch = np.zeros((H, W), bool)
    for x in range(30, 66, 3): stitch |= rect(x, 60, x + 1, 63)
    for y in range(18, 44, 3): stitch |= rect(47, y, 49, y + 1)
    s.paint(stitch & (circle(48, 30, 13) | ellipse(48, 58, 22, 20)), BONE.base)
    s.paint(line(10, 66, 14, 70, 1) | line(14, 66, 10, 70, 1), BONE.base)
    if back: return
    for x in (42, 54):
        s.paint(circle(x, 29, 3.2), '#141420'); s.paint(rect(x - 1, 28, x + 1, 30), BONE.base)
    s.paint(line(40, 37, 56, 37, 1), RAG.outline)

def dream_cruncher(s, back):
    s.add(rect(14, 26, 82, 84), GUNMET)                                                   # compactor box
    s.add(rect(10, 22, 86, 34), CHROME)
    s.add(rect(22, 84, 34, 92), CHROME); s.add(rect(62, 84, 74, 92), CHROME)
    for x in (12, 84): s.add(rect(x - 4, 40, x + 4, 72), CHROME)
    for (x, y, c) in ((4, 14, CYANGLW), (88, 10, HOTPINK), (2, 80, CYANGLW), (90, 86, HOTPINK)):
        s.paint(poly([(x, y + 3), (x + 3, y), (x + 6, y + 3), (x + 3, y + 7)]), c, clip=False)
    if back:
        for y in (40, 50, 60, 70): s.paint(rect(18, y, 78, y + 2), GUNMET.light); return
    s.add(rect(20, 50, 76, 78), R('#0a0a10', '#18181f', '#2a0f18', '#3a1420'))             # maw
    for x in range(22, 76, 7):
        s.paint(poly([(x, 50), (x + 6, 50), (x + 3, 57)]), '#ffffff')
        s.paint(poly([(x, 78), (x + 6, 78), (x + 3, 71)]), '#ffffff')
    s.paint(rect(30, 62, 34, 66), CYANGLW); s.paint(rect(60, 64, 63, 67), HOTPINK)
    glow_eye(s, 28, 38, 12, RED); glow_eye(s, 56, 38, 12, RED)

DESIGNS = {
 '001': mochii, '002': tiidebiite, '003': aquari_os, '004': razorgater, '005': chromedile, '006': reaperdile,
 '007': tyrage, '008': duneclaw, '009': oblivirex, '010': kittember, '011': pyropaw, '012': manticlaw,
 '013': pupbble, '014': terradog, '015': quakehound, '016': squirmite, '017': cocoonode, '018': mothrix,
 '019': zephling, '020': aerobeak, '021': stormtalon, '022': finblade, '023': megalochrome, '024': floatcalf,
 '025': astroleviathan, '026': inklet, '027': toxitacle, '028': krakenox, '029': punchkid, '030': strikechamp,
 '031': kickmaster, '032': gearkid, '033': mechapion, '034': gorokappa, '035': pebblefist, '036': cragarm,
 '037': terrapod, '038': sproutle, '039': shellguard, '040': dreadtoise, '041': pixilite, '042': wispkin,
 '043': duskfiend, '044': ashemit, '045': pyromonk, '046': yogiferno, '331': mythar,
 'BS-02': emburrn, 'BS-03': aquabble, 'DIW-01': mochling, 'DIW-02': glitch_mochi, 'DIW-03': neon_stalker,
 'DIW-04': ragdoll_brute, 'DIW-05': dream_cruncher,
}
