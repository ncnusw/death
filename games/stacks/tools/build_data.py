"""Builds data.js for 書庫裡的光 Light in the Stacks. Run from this folder: python3 build_data.py
Maps are drawn here in code so every row has the right length; the story script, quizzes and passwords are in story.py.
Edit those, then run this again. It also checks that every door and person can be reached, and places the shadows
so that each one crosses the route at a junction (you can wait for it to pass) instead of blocking a corridor."""
import json, pathlib, collections, random, re
import story

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / 'data.js'
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def blank(w, h, ch='.'):
    return [[ch] * w for _ in range(h)]

# ---------------------------------------------------------------- legend
LEGEND = {
    'ground': {
        'f': ['dungeon', 48, 0], 'W': ['dungeon', 40, 1], 'V': ['dungeon', 28, 1], '+': ['dungeon', 42, 0],
        'c': ['extra', 2, 0], 'u': ['extra', 3, 0], 'B': ['extra', 0, 1], 'b': ['extra', 1, 1],
        's': ['extra', 4, 0], 'S': ['extra', 5, 0]},
    'obj': {
        '1': ['dungeon', 72, 1], '2': ['dungeon', 73, 0], '7': ['extra', 9, 1], '8': ['extra', 10, 1], '9': ['extra', 11, 1],
        'B': ['extra', 0, 1], 'b': ['extra', 1, 1], 'F': ['extra', 6, 1], 'L': ['extra', 8, 1], 'P': ['extra', 7, 1], 'D': ['extra', 13, 1]}}
SOLID_G = {k for k, v in LEGEND['ground'].items() if v[2]}
SOLID_O = {k for k, v in LEGEND['obj'].items() if v[2]}

# ---------------------------------------------------------------- lecture hall (opening and ending): 20 x 21, 60 seats
CW, CH = 20, 21
cg = ['W' * CW, 'W' * CW] + ['W' + 'f' * (CW - 2) + 'W' for _ in range(CH - 3)] + ['W' * 10 + '+' + 'W' * (CW - 11)]
co = blank(CW, CH)
co[1][6] = '7'
for x in range(7, 13): co[1][x] = '8'
co[1][13] = '9'
for x in (9, 10, 11): co[3][x] = '1'
SEAT_COLS = [2, 3, 4, 5, 8, 9, 10, 11, 14, 15, 16, 17]
SEAT_ROWS = [6, 9, 12, 15, 18]
for y in SEAT_ROWS:
    for x in SEAT_COLS: co[y - 1][x] = '1'
classroom = {'ground': cg, 'obj': [''.join(r) for r in co], 'doors': {'out': {'x': 10, 'y': CH - 1, 'locked': True, 'msg': '還沒下課，不能離開教室。'}}}
PLAYER_SEAT = (16, 18)
TALKERS = {(15, 18): 'cls_a', (17, 18): 'cls_b', (11, 18): 'cls_c'}
def classroom_puts(with_labels=True):
    looks = ['v2', 'v3', 'v5', 'v6', 'v7', 'v8', 'v9', 'hao', 'kid', 'li']
    out, n = [], 0
    for y in SEAT_ROWS:
        for x in SEAT_COLS:
            if (x, y) == PLAYER_SEAT: continue
            lab = TALKERS.get((x, y), '-') if with_labels else '-'
            look = looks[(n * 3 + y) % len(looks)]
            if look == 'hao': look = 'v6'          # keep Zhe's look for Zhe
            out.append(f"@put s{n} {look} classroom {x} {y} {lab}{' !' if lab != '-' else ''}")
            n += 1
    return '\n'.join(out)

# ---------------------------------------------------------------- library, ground floor: 24 x 16
LW, LH = 24, 16
lg = [list('W' * LW), list('W' * LW)] + [list('W' + 'c' * (LW - 2) + 'W') for _ in range(LH - 3)] + [list('W' * 12 + '+' + 'W' * 11)]
for x in (3, 7, 16, 20): lg[1][x] = 'V'
lg[2][22] = 's'                                  # stairs down to the lower stacks
lo = blank(LW, LH)
def shelf_row(grid, y, x0, x1):
    for x in range(x0, x1 + 1): grid[y][x] = 'B' if (x + y) % 3 else 'b'
for y in (4, 7, 10): shelf_row(lo, y, 2, 8)
for y in (4, 7, 10): shelf_row(lo, y, 15, 20)
for x in (11, 12, 13): lo[5][x] = '1'; lo[9][x] = '1'
for x in (11, 13): lo[4][x] = '2'; lo[6][x] = '2'; lo[8][x] = '2'; lo[10][x] = '2'
lo[12][20] = '1'; lo[12][21] = '1'               # Zhe's corner table
for x in (2, 3, 4, 5): lo[12][x] = 'D'           # circulation desk
lo[2][1] = 'P'; lo[14][1] = 'P'; lo[14][22] = 'P'
library = {'ground': [''.join(r) for r in lg], 'obj': [''.join(r) for r in lo], 'doors': {
    'out': {'x': 12, 'y': LH - 1, 'to': 'counsel', 'tx': 6, 'ty': 7, 'dir': 'up'},
    'basement': {'x': 22, 'y': 2, 'to': 'b1', 'tx': 1, 'ty': 1, 'dir': 'down'}}}

# ---------------------------------------------------------------- counseling center: 13 x 9
KW, KH = 13, 9
kg = ['W' * KW, 'WW' + 'V' + 'W' * (KW - 6) + 'V' + 'WW'] + ['W' + 'c' * (KW - 2) + 'W' for _ in range(KH - 3)] + ['W' * 6 + '+' + 'W' * 6]
ko = blank(KW, KH)
ko[1][6], ko[1][7], ko[1][8] = '7', '8', '9'     # whiteboard
ko[2][2] = 'F'; ko[2][3] = 'F'                   # sofa
ko[3][2] = 'L'                                   # low table with tissues
ko[4][10] = '1'; ko[4][11] = '1'                 # desk
ko[2][11] = 'P'; ko[6][1] = 'P'
counsel = {'ground': kg, 'obj': [''.join(r) for r in ko], 'doors': {
    'out': {'x': 6, 'y': KH - 1, 'to': 'library', 'tx': 12, 'ty': 14, 'dir': 'up'}}}

# ---------------------------------------------------------------- the lower stacks: three mazes of bookshelves
def make_maze(cw, ch, seed, extra):
    rng = random.Random(seed)
    tw, th = cw * 2 + 1, ch * 2 + 1
    t = [['#'] * tw for _ in range(th)]
    seen = {(0, 0)}; stack = [(0, 0)]; t[1][1] = 'u'
    while stack:
        cx, cy = stack[-1]
        nb = [(cx + dx, cy + dy, dx, dy) for dx, dy in DIRS if 0 <= cx + dx < cw and 0 <= cy + dy < ch and (cx + dx, cy + dy) not in seen]
        if not nb: stack.pop(); continue
        nx, ny, dx, dy = rng.choice(nb)
        t[cy * 2 + 1 + dy][cx * 2 + 1 + dx] = 'u'; t[ny * 2 + 1][nx * 2 + 1] = 'u'
        seen.add((nx, ny)); stack.append((nx, ny))
    for _ in range(extra):       # a few extra openings, so there is more than one way round
        while True:
            x, y = rng.randrange(1, tw - 1), rng.randrange(1, th - 1)
            if t[y][x] == '#' and ((t[y][x - 1] == 'u' and t[y][x + 1] == 'u' and t[y - 1][x] == '#' and t[y + 1][x] == '#') or
                                   (t[y - 1][x] == 'u' and t[y + 1][x] == 'u' and t[y][x - 1] == '#' and t[y][x + 1] == '#')):
                t[y][x] = 'u'; break
    return t

def finish_maze(t, mirror, up, down):
    th, tw = len(t), len(t[0])
    if mirror: t = [r[::-1] for r in t]
    g = []
    for y, r in enumerate(t):
        row = []
        for x, c in enumerate(r):
            if c == 'u': row.append('u')
            elif x in (0, tw - 1) or y in (0, th - 1): row.append('W')       # stone outer wall
            else: row.append('B' if (x * 3 + y * 5) % 4 else 'b')            # bookshelves inside
        g.append(row)
    g[up[1]][up[0]] = 'S'
    if down: g[down[1]][down[0]] = 's'
    return [''.join(r) for r in g], ['.' * tw for _ in g]

def bfs(g, start):
    d = {start: 0}; prev = {start: None}; q = collections.deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            n = (x + dx, y + dy)
            if 0 <= n[1] < len(g) and 0 <= n[0] < len(g[0]) and g[n[1]][n[0]] == 'u' and n not in d:
                d[n] = d[(x, y)] + 1; prev[n] = (x, y); q.append(n)
    return d, prev

def path(prev, end):
    p = []
    while end is not None: p.append(end); end = prev[end]
    return p[::-1]

def place_shadows(g, start, goal, n, seed, avoid=()):
    """Shadows patrol straight 3-5 tile runs that cross the shortest route at exactly one tile (a junction),
    so you can always wait beside the junction for the shadow to pass. Far from the stairs, spread out."""
    rng = random.Random(seed)
    d, prev = bfs(g, start)
    route = set(path(prev, goal))
    cands = []
    h, w = len(g), len(g[0])
    floor = {(x, y) for y in range(h) for x in range(w) if g[y][x] == 'u'}
    for horiz in (True, False):
        for a in range(h if horiz else w):
            runs, cur = [], []
            for b in range(w if horiz else h):
                p = (b, a) if horiz else (a, b)
                if p in floor: cur.append(p)
                else:
                    if len(cur) >= 3: runs.append(cur)
                    cur = []
            if len(cur) >= 3: runs.append(cur)
            for run in runs:
                for L in (5, 4, 3):
                    for i in range(len(run) - L + 1):
                        seg = run[i:i + L]
                        on = [p for p in seg if p in route]
                        if len(on) != 1: continue
                        if min(d[p] for p in seg) < 6: continue
                        if any(abs(p[0] - q[0]) + abs(p[1] - q[1]) <= 2 for p in seg for q in (goal,) + tuple(avoid)): continue
                        # the tile before the junction on the route must be a safe place to wait (not on the run)
                        cands.append((seg, on[0]))
    rng.shuffle(cands)
    chosen = []
    while len(chosen) < n and cands:
        def score(c):
            if not chosen: return d[c[1]]
            return min(abs(c[1][0] - o[1][0]) + abs(c[1][1] - o[1][1]) for o in chosen) * 3 + len(c[0])
        cands.sort(key=score, reverse=True)
        best = cands.pop(0)
        if any(set(best[0]) & set(o[0]) for o in chosen): continue
        chosen.append(best)
    assert len(chosen) == n, f'only {len(chosen)} shadow places found'
    return [(seg[0], seg[-1]) for seg, _ in chosen], len(route) - 1

# B1: small and gentle. Up stairs top-left, down stairs bottom-right.
t1 = make_maze(8, 5, 2026108, 7)
tw1, th1 = len(t1[0]), len(t1)
b1g, b1o = finish_maze(t1, False, (1, 0), (tw1 - 2, th1 - 1))
# B2: a bit bigger, mirrored: up stairs top-right, down stairs bottom-left.
t2 = make_maze(10, 6, 2026208, 6)
tw2, th2 = len(t2[0]), len(t2)
b2g, b2o = finish_maze(t2, True, (tw2 - 2, 0), (1, th2 - 1))
# B3: the big one. Zhe waits in a dead end that is a real detour; no stairs further down.
t3 = make_maze(13, 9, 2026308, 4)
tw3, th3 = len(t3[0]), len(t3)
b3g, b3o = finish_maze(t3, False, (1, 0), None)

B1_START, B1_GOAL = (1, 1), (tw1 - 2, th1 - 2)
B2_START, B2_GOAL = (tw2 - 2, 1), (1, th2 - 2)
B3_START = (1, 1)
d3, _ = bfs(b3g, B3_START)
dead = [c for c in d3 if sum(b3g[c[1] + b][c[0] + a] == 'u' for a, b in DIRS) == 1 and c != B3_START]
ZHE = max(dead, key=lambda c: d3[c])
B3_STEPS = d3[ZHE]

shadows = {}
shadows['b1'], _ = place_shadows(b1g, B1_START, B1_GOAL, len(story.SHADOWS['b1']), 11)
shadows['b2'], _ = place_shadows(b2g, B2_START, B2_GOAL, len(story.SHADOWS['b2']), 12)
shadows['b3'], _ = place_shadows(b3g, B3_START, ZHE, len(story.SHADOWS['b3']), 13)

b1 = {'ground': b1g, 'obj': b1o, 'doors': {
    'up': {'x': 1, 'y': 0, 'locked': True, 'msg': '阿哲還在下面。'},
    'down': {'x': tw1 - 2, 'y': th1 - 1, 'to': 'b2', 'tx': B2_START[0], 'ty': B2_START[1], 'dir': 'down'}}}
b2 = {'ground': b2g, 'obj': b2o, 'doors': {
    'up': {'x': tw2 - 2, 'y': 0, 'locked': True, 'msg': '阿哲還在更下面。'},
    'down': {'x': 1, 'y': th2 - 1, 'to': 'b3', 'tx': 1, 'ty': 1, 'dir': 'down'}}}
b3 = {'ground': b3g, 'obj': b3o, 'doors': {'up': {'x': 1, 'y': 0, 'locked': True, 'msg': '阿哲就在這一層。'}}}

MAPS = {'classroom': classroom, 'library': library, 'counsel': counsel, 'b1': b1, 'b2': b2, 'b3': b3}

# ---------------------------------------------------------------- characters & speakers
CHARS = ['an', 'lin', 'v2', 'v3', 'mei', 'v5', 'v6', 'v7', 'v8', 'v9', 'chen', 'hao', 'wu', 'kid', 'me', 'li', 'chief']
SPEAKERS = {
    'Me': {'name': '你', 'sprite': 'me', 'vo': '你（心裡想）'},
    'Teacher': {'name': '老師', 'sprite': 'D:88'},
    'Classmate': {'name': '同學', 'sprite': 'v5'},
    'Zhe': {'name': '阿哲', 'sprite': 'hao'},
    'Hsu': {'name': '許老師（諮商心理師）', 'sprite': 'v3'},
    'Librarian': {'name': '館員阿姨', 'sprite': 'lin'},
    'Phone': {'name': '📱 手機', 'sprite': None},
}

TEXT = {
    'locked': '門鎖著。',
    'idle': '走到人或東西旁邊，按 A 說話。頭上有 ! 的地方有新的事。',
    'choose': '你會怎麼做？',
    'right': '答對了！',
    'hintLead': '再想想：',
    'pauseHead': '⏸ 暫停',
    'waitFor': '{s} 後可以繼續。',
    'pickFirst': '請先選一個答案。',
    'badCode': '密碼不對。請看老師投影片上的密碼。',
    'newTerm': '新名詞 ',
    'endStats': '許老師的小考，第一次就答對：<b>{f} / {n}</b> 題',
}

# ---------------------------------------------------------------- script
_ids = {}
for line in classroom_puts().split('\n'):
    parts = line.split()
    if parts[6] != '-': _ids[parts[6]] = parts[1]
mob_lines = []
for floor in ('b1', 'b2', 'b3'):
    for i, ((sprite, name), (a, b)) in enumerate(zip(story.SHADOWS[floor], shadows[floor])):
        mob_lines.append(f'@mob {floor}m{i} {sprite} {floor} {a[0]} {a[1]} {b[0]} {b[1]} {story.SHADOW_MS[floor]} hit_{floor} {name}')
SCRIPT = (story.SCRIPT.replace('{{CLASSROOM}}', classroom_puts()).replace('{{CLASSROOM_PLAIN}}', classroom_puts(False))
          .replace('{{MOBS}}', '\n'.join(mob_lines))
          .replace('{{ZX}}', str(ZHE[0])).replace('{{ZY}}', str(ZHE[1])).replace('{{B2X}}', str(B2_START[0]))
          .replace('{{B3_SECONDS}}', str(story.b3_seconds(B3_STEPS))).replace('{{B3_SECONDS_LONG}}', str(story.b3_seconds(B3_STEPS, 1.5)))
          .replace('{{A}}', _ids['cls_a'][1:]).replace('{{B}}', _ids['cls_b'][1:]).replace('{{C}}', _ids['cls_c'][1:]))
assert '{{' not in SCRIPT, re.findall(r'\{\{\w+\}\}', SCRIPT)

data = {
    'id': 'stacks-v1', 'start': 'intro', 'player': 'me',
    'assets': {'dungeon': '../../assets/tiles/tinydungeon.png', 'chars': '../../assets/tiles/characters.png', 'extra': 'extra.png'},
    'chars': CHARS, 'legend': LEGEND, 'maps': MAPS, 'speakers': SPEAKERS, 'terms': {}, 'quizzes': story.QUIZZES, 'pauses': story.PAUSES,
    'jumps': story.JUMPS, 'hashJumps': {}, 'text': TEXT,
}

# ---------------------------------------------------------------- checks
def walkable(m, x, y):
    gr, ob = m['ground'], m['obj']
    if not (0 <= y < len(gr) and 0 <= x < len(gr[0])): return False
    return gr[y][x] not in SOLID_G and ob[y][x] not in SOLID_O

def reach(m, sx, sy):
    seen = {(sx, sy)}; q = collections.deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            n = (x + dx, y + dy)
            if n not in seen and walkable(m, *n): seen.add(n); q.append(n)
    return seen
def adj(seen, x, y): return any((x + a, y + b) in seen for a, b in DIRS)

for mid, m in MAPS.items():
    w = len(m['ground'][0])
    assert all(len(r) == w for r in m['ground'] + m['obj']), mid
    assert len(m['ground']) == len(m['obj']), mid
    for r in m['ground']:
        for c in r: assert c in LEGEND['ground'], (mid, c)
    for r in m['obj']:
        for c in r: assert c == '.' or c in LEGEND['obj'], (mid, c)
    for did, dd in m['doors'].items():
        if dd.get('to'): assert walkable(MAPS[dd['to']], dd['tx'], dd['ty']), f'{mid}/{did} lands on a wall'
STARTS = {'classroom': [PLAYER_SEAT], 'library': [(12, 14)], 'counsel': [(6, 7)], 'b1': [B1_START], 'b2': [B2_START], 'b3': [B3_START]}
for mid, m in MAPS.items():
    seen = set()
    for s in STARTS[mid]: seen |= reach(m, *s)
    for did, dd in m['doors'].items(): assert adj(seen, dd['x'], dd['y']), f'cannot reach door {mid}/{did}'
assert B1_GOAL in reach(b1, *B1_START) and B2_GOAL in reach(b2, *B2_START) and ZHE in reach(b3, *B3_START)
labels = set(re.findall(r'^:: (\S+)', SCRIPT, re.M))
for m in re.finditer(r'^@put (\S+) (\S+) (\S+) (\d+) (\d+) (\S+)', SCRIPT, re.M):
    _id, spr, mp, x, y, lab = m.groups()
    assert lab == '-' or lab in labels, f'@put {_id}: unknown label {lab}'
    assert spr in CHARS or re.match(r'^[TDX]:\d+$', spr), spr
    if spr.startswith('X:'): continue                     # things on walls (notice board)
    assert walkable(MAPS[mp], int(x), int(y)), f'@put {_id} on a blocked tile {mp} {x},{y}'
    if lab != '-':
        seen = set()
        for s in STARTS[mp]: seen |= reach(MAPS[mp], *s)
        assert adj(seen, int(x), int(y)), f'cannot walk up to {_id} on {mp} {x},{y}'
for m in re.finditer(r'^@(?:goto|label \S+) (\S+)', SCRIPT, re.M): assert m.group(1) == '-' or m.group(1) in labels, m.group(0)
for m in re.finditer(r'^@if \S+ (\S+)', SCRIPT, re.M): assert m.group(1) in labels, m.group(0)
for m in re.finditer(r'^@(?:zone \S+ \S+ \S+ \S+ \S+ \S+|timer \S+) (\S+)', SCRIPT, re.M): assert m.group(1) in labels, m.group(0)
for m in re.finditer(r'-> (\S+)', SCRIPT): assert m.group(1) in labels, m.group(0)
for m in re.finditer(r'^@quiz (\S+)', SCRIPT, re.M): assert m.group(1) in story.QUIZZES, m.group(0)
for m in re.finditer(r'^@pause (\S+)', SCRIPT, re.M): assert m.group(1) in story.PAUSES, m.group(0)
for m in re.finditer(r'^([A-Za-z][A-Za-z .]*?)(?: \(VO\))?: ', SCRIPT, re.M): assert m.group(1) in SPEAKERS, m.group(1)
assert set(story.QUIZZES) == set(re.findall(r'^@quiz (\S+)', SCRIPT, re.M)), 'every quiz should be used'
for q in story.QUIZZES.values(): assert 0 <= q['answer'] < len(q['options'])
for jump in story.JUMPS.values(): assert jump in labels
# every shadow walks only on floor
for floor, segs in shadows.items():
    for (a, b) in segs:
        for i in range(abs(a[0] - b[0]) + abs(a[1] - b[1]) + 1):
            x = a[0] + i * (b[0] > a[0]) - i * (b[0] < a[0]); y = a[1] + i * (b[1] > a[1]) - i * (b[1] < a[1])
            assert MAPS[floor]['ground'][y][x] == 'u', (floor, a, b)

js = ('/* 書庫裡的光 Light in the Stacks — chapter data for the story-walk engine (../engine/engine.js).\n'
      ' * GENERATED by tools/build_data.py. Edit tools/story.py (story, quizzes, passwords, discussion question) or build_data.py (maps) and run build_data.py again.\n'
      ' * Content follows the Week 8 lecture, Grief Counseling & Prolonged Grief (DSM-5-TR; Prigerson et al., 2021). The campus and all its people are fictional.\n'
      ' * Art: Tiny Dungeon by Kenney (www.kenney.nl), CC0 1.0; characters from the IntroSW site (Kenney-based, CC0); extra.png drawn for this site (CC0). */\n'
      'window.GAME = ' + json.dumps(data, ensure_ascii=False, indent=1) + ';\n'
      'window.GAME.script = ' + json.dumps(SCRIPT, ensure_ascii=False) + ';\n')
OUT.write_text(js, encoding='utf-8')
if __name__ == '__main__':
    for name, g in (('b1', b1g), ('b2', b2g), ('b3', b3g)):
        print(name, len(g[0]), 'x', len(g)); segs = shadows[name]
        rows = [list(r) for r in g]
        for (a, b) in segs:
            for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1): rows[y][x] = '@'
        if name == 'b3': rows[ZHE[1]][ZHE[0]] = 'Z'
        print('\n'.join(''.join(r).replace('B', '#').replace('b', '#').replace('u', ' ') for r in rows))
    print('B3: Zhe at', ZHE, 'shortest route', B3_STEPS, 'steps; time limit', story.b3_seconds(B3_STEPS), 's')
    print('wrote', OUT, len(js), 'bytes;', len(labels), 'labels,', len(story.QUIZZES), 'quizzes')
