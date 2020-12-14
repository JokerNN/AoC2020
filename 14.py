from collections import defaultdict
import re

with open('inp14.txt') as f:
    inp = f.read()

# inp = '''mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# '''


def apply_mask(num: int, mask: str):
    ns = list("{0:036b}".format(num))
    for idx, c in enumerate(mask):
        if c != 'X':
            ns[idx] = c
    
    return int(''.join(ns), 2)


mask = ''
mem = defaultdict(int)
mem_re = re.compile(r'mem\[(?P<addr>\d+)\] = (?P<value>\d+)')


for line in inp.strip().split('\n'):
    if line.startswith('mask'):
        mask = line.replace('mask = ', '')

    if line.startswith('mem'):
        m = mem_re.match(line)
        addr = int(m.group('addr'))
        value = int(m.group('value'))

        value = apply_mask(value, mask)
        mem[addr] = value

print('Part 1.', sum(mem.values()))


def apply_mask2(num: int, mask: str):
    ns = list("{0:036b}".format(num))
    for idx, c in enumerate(mask):
        if c != '0':
            ns[idx] = c
    
    return ''.join(ns)


def replace_floating(mask: str, num_s: str):
    mask_list = list(mask)
    rp = -1
    for idx, c in reversed(list(enumerate(mask_list))):
        if c == 'X':
            mask_list[idx] = num_s[rp]
            rp -= 1

    return int(''.join(mask_list), 2)


mem = defaultdict(int)

for line in inp.strip().split('\n'):
    if line.startswith('mask'):
        mask = line.replace('mask = ', '')

    if line.startswith('mem'):
        m = mem_re.match(line)
        addr_mask = int(m.group('addr'))
        value = int(m.group('value'))

        addr_mask = apply_mask2(addr_mask, mask)
        fl_count = addr_mask.count('X')
        for idx in range(2 ** fl_count):
            addr = replace_floating(addr_mask, "{0:036b}".format(idx))
            mem[addr] = value


print('Part 2.', sum(mem.values()))

    




    


