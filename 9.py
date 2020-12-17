from collections import Counter

inp = ''

with open('inputs/inp9.txt') as f:
    inp = f.read()

nums = [int(n) for n in inp.split('\n')]

counts = set(nums[:25])

invalid_number = None

for idx, n in enumerate(nums[25:], 25):
    found_pair = False

    for k in counts:
        if n - k in counts:
            found_pair = True
            break

    if not found_pair:
        invalid_number = n
        break

    counts.discard(nums[idx - 25])
    counts.add(n)


print('Part 1.', invalid_number)

ps = 0
pe = 0
s = nums[0]

while s != invalid_number:
    if s < invalid_number:
        pe += 1
        s += nums[pe]
    elif s > invalid_number:
        s -= nums[ps]
        ps += 1

sumset = nums[ps:pe + 1]

print('Part 2.', min(sumset) + max(sumset))
        