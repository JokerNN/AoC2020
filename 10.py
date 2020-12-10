from functools import lru_cache

with open('./inp10.txt') as f:
    inp = f.read()

# inp = '''16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# '''

# inp = '''28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3'''

adapters = sorted([int(n) for n in inp.strip().split('\n')])
adapters.append(adapters[-1] + 3)

d1 = 1
d3 = 0
for idx, n in enumerate(adapters):
    diff = n - adapters[idx - 1]
    if diff == 1:
        d1 += 1
    if diff == 3:
        d3 += 1

print('Part 1.', d1 * d3)

adapters = [0, *adapters]

@lru_cache(None)
def count_ways(idx):
    if idx == 0:
        return 1

    if idx < 0:
        return 0

    res = 0
    cur_adapter = adapters[idx]

    idx -= 1
    while idx >= 0 and cur_adapter - adapters[idx] <= 3:
        res += count_ways(idx)
        idx -= 1

    return res

print('Part 2.', count_ways(len(adapters) - 1))
