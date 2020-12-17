f = open('inputs/inp5.txt')

inp = f.read()

max_sid = -float('inf')
min_sid = float('inf')
sid_set = set()

for line in inp.split('\n'):
    ssid = line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    sid = int(ssid, 2)
    min_sid = min(sid, min_sid)
    max_sid = max(sid, max_sid)
    sid_set.add(sid)

print('Part 1.', max_sid)

for sid in range(min_sid + 1, max_sid):
    if sid not in sid_set and sid - 1 in sid_set and sid + 1 in sid_set:
        print('Part 2.', sid)
