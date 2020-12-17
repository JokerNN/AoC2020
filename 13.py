from chinese_remainder_theorem import chinese_remainder

with open('inputs/inp13.txt') as f:
    inp = f.read()

# inp = '''
# 939
# 7,13,x,x,59,x,31,19
# '''

# inp = '''
# 1
# 17,x,13,19
# '''

# inp = '''
# 0
# 67,7,59,61
# '''
    
# inp = '''
# 0
# 67,x,7,59,61
# '''
    
# # inp = '''
# # 0
# # 67,7,x,59,61
# # '''
    
# inp = '''
# 0
# 1789,37,47,1889
# '''


s_ts, schedule = inp.strip().split('\n')

ts = int(s_ts)
bus_ids = [int(b_id) for b_id in schedule.split(',') if b_id != 'x']

# print(ts, bus_ids)

min_wait = float('inf')
min_bid = None

for bid in bus_ids:
    wait = bid - ts % bid
    if min_wait > wait:
        min_wait = wait
        min_bid = bid

print('Part 1', min_wait * min_bid)

schedule = inp.strip().split('\n')[1]
bus_ids = {}
for idx, bid in enumerate(schedule.split(',')):
    if bid != 'x':
        bid = int(bid)
        bus_ids[bid] = bid - idx % bid


print('Part 2', chinese_remainder(bus_ids.keys(), bus_ids.values()))