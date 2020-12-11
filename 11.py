from copy import deepcopy

with open('./inp11.txt') as f:
    inp = f.read()


# inp = '''
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# '''

def stringify_map(sm):
    return '\n'.join(''.join(row) for row in sm)

def count_occupied_seats(sm, r_idx, s_idx):
    tl = sm[r_idx - 1][s_idx - 1]
    tt = sm[r_idx - 1][s_idx]
    tr = sm[r_idx - 1][s_idx + 1]
    ll = sm[r_idx][s_idx - 1]
    rr = sm[r_idx][s_idx + 1]
    bl = sm[r_idx + 1][s_idx - 1]
    bb = sm[r_idx + 1][s_idx]
    br = sm[r_idx + 1][s_idx + 1]
    
    return sum(s == '#' for s in (tl, tt, tr, ll, rr, bl, bb, br))

def project_vector(sm, r_idx, s_idx, vector):
    r, s = r_idx, s_idx
    r += vector[0]
    s += vector[1]
    while r >= 0 and r < len(sm) and s >= 0 and s < len(sm[0]):
        if sm[r][s] != '.':
            return sm[r][s]
        
        r += vector[0]
        s += vector[1]

    return '.'

def count_visibly_occupied_seats(sm, r_idx, s_idx):
    tl = project_vector(sm, r_idx, s_idx, (-1, -1))
    tt = project_vector(sm, r_idx, s_idx, (-1,  0)) 
    tr = project_vector(sm, r_idx, s_idx, (-1,  1))
    ll = project_vector(sm, r_idx, s_idx, ( 0, -1))
    rr = project_vector(sm, r_idx, s_idx, ( 0,  1))
    bl = project_vector(sm, r_idx, s_idx, ( 1, -1))
    bb = project_vector(sm, r_idx, s_idx, ( 1,  0))
    br = project_vector(sm, r_idx, s_idx, ( 1,  1))

    return sum(s == '#' for s in (tl, tt, tr, ll, rr, bl, bb, br))

def cycle(sm):
    next_state = deepcopy(sm)
    change_happened = False
    for r_idx, row in enumerate(sm):
        for s_idx, seat in enumerate(row):
            if seat == 'L':
                sc = count_occupied_seats(sm, r_idx, s_idx)
                if sc == 0:
                    next_state[r_idx][s_idx] = '#'
                    change_happened = True
            elif seat == '#':
                sc = count_occupied_seats(sm, r_idx, s_idx)
                if sc >= 4:
                    next_state[r_idx][s_idx] = 'L'
                    change_happened = True


    return next_state, change_happened

def cycle2(sm):
    next_state = deepcopy(sm)
    change_happened = False
    for r_idx, row in enumerate(sm):
        for s_idx, seat in enumerate(row):
            if seat == 'L':
                sc = count_visibly_occupied_seats(sm, r_idx, s_idx)
                if sc == 0:
                    next_state[r_idx][s_idx] = '#'
                    change_happened = True
            elif seat == '#':
                sc = count_visibly_occupied_seats(sm, r_idx, s_idx)
                if sc >= 5:
                    next_state[r_idx][s_idx] = 'L'
                    change_happened = True


    return next_state, change_happened


seatmap = [['.', *list(row), '.'] for row in inp.strip().split('\n')]
seatmap = [['.'] * len(seatmap[0]), *seatmap, ['.'] * len(seatmap[0])]

while True:
    ns, changed = cycle(seatmap)
    seatmap = ns
    if not changed:
        break

print('Part 1.', stringify_map(seatmap).count('#'))


seatmap = [['.', *list(row), '.'] for row in inp.strip().split('\n')]
seatmap = [['.'] * len(seatmap[0]), *seatmap, ['.'] * len(seatmap[0])]

while True:
    ns, changed = cycle2(seatmap)
    seatmap = ns
    if not changed:
        break

print('Part 2.', stringify_map(seatmap).count('#'))