import os, sys
from functools import partial

f = open(os.path.dirname(os.path.realpath(sys.argv[0]))
 + '/inp3.txt')

inp = f.read()

inp = inp.split('\n')
pos_x = 0
tc = 0
for line in inp:
    if line[pos_x] == '#':
        tc += 1

    pos_x = (pos_x + 3) % len(line)


print("Part 1.", tc)

def traverse(lines, slope):
    pos = {
        'x': 0,
        'y': 0
    }
    tc = 0
    while pos['y'] < len(lines):
        if lines[pos['y']][pos['x']] == '#':
            tc += 1

        pos['x'] = (slope['x'] + pos['x']) % len(lines[0])
        pos['y'] += slope['y']

    return tc

ptraverse = partial(traverse, inp)

res_2 = ptraverse({'x': 1, 'y': 1}) * ptraverse({'x': 3, 'y': 1}) * ptraverse({'x': 5, 'y': 1}) * \
    ptraverse({'x': 7, 'y': 1}) * ptraverse({'x': 1, 'y': 2})

print("Part 2.", res_2)