"""Draws extra.png for Light in the Stacks (bookshelves, carpet, basement floor, stairs, sofa, plant, blackboard)
in the Kenney Tiny Dungeon palette. Run once from this folder: python3 make_tiles.py
Original pixel art for this site, released under CC0 like the Kenney tiles."""
from PIL import Image
import pathlib

OUT = pathlib.Path(__file__).with_name('extra.png')
INK = (63, 38, 49)
WO, WOD, WOL = (189, 108, 74), (118, 59, 54), (234, 165, 108)       # wood
ST, STD, STL = (139, 155, 180), (82, 96, 124), (192, 203, 220)      # stone
BOOKS = [(201, 74, 74), (88, 141, 196), (98, 160, 92), (226, 183, 82), (150, 98, 170), (222, 222, 205), (68, 112, 150)]
CARPET, CARPETD, CARPETL = (84, 104, 118), (70, 88, 102), (98, 120, 134)
CON, COND, CONL = (58, 60, 72), (48, 50, 61), (70, 72, 86)

img = Image.new('RGBA', (192, 32), (0, 0, 0, 0))
px = img.load()

def tile(i, f):
    ox, oy = (i % 12) * 16, (i // 12) * 16
    for y in range(16):
        for x in range(16):
            c = f(x, y)
            if c: px[ox + x, oy + y] = c + (255,)

def shelf(seed):
    def f(x, y):
        if x in (0, 15) or y in (0, 15): return INK
        if x in (1, 14) or y in (1, 7, 8, 14): return WOD if y in (8, 14) or x in (1, 14) else WO
        # two rows of book spines: rows 2-6 and 9-13
        row = 0 if y < 8 else 1
        k = (x * 7 + row * 5 + seed * 3) // 2
        col = BOOKS[(k * 5 + seed + row) % len(BOOKS)]
        top = 2 + ((x + seed + row) % 3 == 0) if row == 0 else 9 + ((x * 3 + seed) % 4 == 0)
        if y < top: return INK
        if x % 2 == 0 and (x + seed + row) % 5 == 0: return INK          # gap between books
        if y == top + 1 and x % 3 == 1: return tuple(min(255, c + 40) for c in col)
        return col
    return f
tile(0, shelf(0))
tile(1, shelf(3))

# 2: library carpet
tile(2, lambda x, y: CARPETD if (x + y) % 8 == 0 else (CARPETL if (x * 3 + y * 5) % 23 == 0 else CARPET))
# 3: basement concrete
tile(3, lambda x, y: COND if (x * 5 + y * 3) % 13 == 0 else (CONL if (x * 7 + y * 11) % 29 == 0 else (COND if y == 15 or x == 15 else CON)))

# 4: stairs going down (steps get darker), 5: stairs going up
def stairs(down):
    def f(x, y):
        if x in (0, 15): return INK
        if x in (1, 14): return STD
        step = y // 4
        k = step if down else 3 - step
        base = [STL, ST, STD, (50, 56, 76)][k]
        if y % 4 == 3: return INK if down else STD
        return base
    return f
tile(4, stairs(True))
tile(5, stairs(False))

# 6: sofa (front), 7: potted plant
SOF, SOFD, SOFL = (110, 140, 120), (78, 104, 90), (150, 180, 150)
def sofa(x, y):
    if y < 3 or y > 14: return None
    if y in (3, 14) or x in (0, 15): return INK
    if y < 8: return SOFL if y == 4 else SOF
    if x in (1, 2, 13, 14): return SOFD
    if y == 8: return SOFL
    return SOF if x != 8 else SOFD
tile(6, sofa)
LEAF, LEAFD, POT, POTD = (98, 160, 92), (60, 112, 66), (189, 108, 74), (118, 59, 54)
def plant(x, y):
    if y >= 10:
        if y == 15 or x in (4, 11): return INK if 4 <= x <= 11 else None
        return (POTD if y == 10 else POT) if 4 < x < 11 else None
    d = ((x - 7.5) ** 2 + ((y - 5) * 1.3) ** 2) ** .5
    if d > 6.2: return None
    if d > 5.3: return INK
    return LEAFD if (x * 3 + y) % 5 == 0 else LEAF
tile(7, plant)

# 8: low table with a box of tissues
def table(x, y):
    if y < 5 or y > 14: return None
    if y in (5, 14) and 0 < x < 15 or x in (0, 15) and 5 <= y <= 14: return INK
    if 5 < x < 11 and 2 <= y <= 5:
        return (240, 240, 240) if y > 2 else INK
    if y >= 11: return WOD if x in (2, 13) else None
    return WOL if y == 6 else WO
tile(8, table)

# 9-11: blackboard (left, middle, right) hung on a wall (same as Storm Over Clear Creek)
BB, BBL, CH, FR = (46, 84, 66), (60, 104, 82), (225, 232, 220), (140, 92, 58)
def board(part):
    def f(x, y):
        if y < 2 or y > 13: return None
        if y in (2, 13): return FR
        if part == 0 and x < 2: return FR
        if part == 2 and x > 13: return FR
        if y == 12 and x % 5 == 1: return CH
        if part == 1 and y in (5, 8) and 2 < x < 13 and (x * 3 + y) % 4: return CH
        if part == 0 and y == 6 and 4 < x < 13: return CH
        return BBL if (x + y) % 7 == 0 else BB
    return f
tile(9, board(0)); tile(10, board(1)); tile(11, board(2))

# 12: notice board on a wall (poster for the counseling center)
def notice(x, y):
    if y < 1 or y > 13 or x < 1 or x > 14: return None
    if y in (1, 13) or x in (1, 14): return WOD
    if 3 <= x <= 8 and 3 <= y <= 10: return (238, 226, 196) if not (y in (5, 7) and 4 <= x <= 7) else (120, 110, 100)
    if 10 <= x <= 12 and 4 <= y <= 9: return (143, 211, 255) if y != 6 else (68, 112, 150)
    return (170, 130, 90)
tile(12, notice)
# 13: circulation desk (front)
tile(13, lambda x, y: None if y < 4 else (INK if y in (4, 15) or x in (0, 15) else (WOL if y == 5 else (WOD if y % 5 == 0 else WO))))
# 14: the friend's backpack on the floor (used as an object)
def bag(x, y):
    d = ((x - 7.5) ** 2 + ((y - 9.5) * 1.1) ** 2) ** .5
    if d > 5.6: return None
    if d > 4.7: return INK
    if y == 8: return (40, 70, 110)
    return (68, 112, 150)
tile(14, bag)

img.save(OUT)
print('wrote', OUT)
