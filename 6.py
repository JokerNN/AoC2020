from functools import reduce

inp = ''

with open('inputs/inp6.txt') as f:
    inp = f.read()

res = 0

for group in inp.split('\n\n'):
    lines = (set(l) for l in group.split('\n'))
    r_set = reduce(lambda i, a: a | i, lines)
    res += len(r_set)

print("Part 1.", res)

res2 = 0

for group in inp.split('\n\n'):
    lines = (set(l) for l in group.split('\n'))
    les = reduce(lambda i, a: a & i, lines)
    res2 += len(les)


print("Part 2.", res2)
