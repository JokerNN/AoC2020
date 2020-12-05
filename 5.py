f = open('./inp5.txt')

inp = f.read()

max_sid = -float('inf')
min_sid = float('inf')
sid_set = set()

for line in inp.split('\n'):
    # line = 'FBFBBFFRLR'
    r = line[:7]
    c = line[7:]
    row = r.replace('F', '0').replace('B', '1')
    col = c.replace('L', '0').replace('R', '1')
    row_idx = int(row, 2)
    col_idx = int(col, 2)
    # print(line)
    # print(row, col)
    # print(row_idx, col_idx)
    seat_id = row_idx * 8 + col_idx
    min_sid = min(seat_id, min_sid)
    max_sid = max(seat_id, max_sid)
    sid_set.add(seat_id)

print('Part 1.', max_sid)

for sid in range(min_sid + 1, max_sid):
    if sid not in sid_set and sid - 1 in sid_set and sid + 1 in sid_set:
        print('Part 2.', sid)
