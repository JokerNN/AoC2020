import re
from collections import defaultdict

inp = ''
with open('./inp7.txt') as f:
    inp = f.read()


# inp = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.'''


# inp = '''shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.'''


contains = defaultdict(dict)
contained_by = defaultdict(set)

content_re = re.compile(r'(?P<amount>\d+) (?P<color>[\w\s]+) bags?\.?')

for line in inp.split('\n'):
    container, content = line.split(' bags contain ')

    if content == 'no other bags.':
        continue

    for c in content.split(', '):
        m = content_re.match(c)
        color = m.group('color')
        amount = int(m.group('amount'))
        contained_by[color].add(container)
        contains[container][color] = amount

visited = set()
q = list(contained_by['shiny gold'])

while len(q) > 0:
    c = q.pop(0)
    if c not in visited:
        visited.add(c)
        q.extend(filter(lambda x: x not in visited, contained_by[c]))

print('Part 1.', len(visited))

def count_rec(color):
    if color not in contains:
        return 1

    count = 1
    for c, amount in contains[color].items():
        count += count_rec(c) * amount
    
    return count

print('Part 2.', count_rec('shiny gold') - 1)
