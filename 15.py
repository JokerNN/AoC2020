inp = '2,20,0,4,1,17'
# inp = '3,2,1'

nums = [int(n) for n in inp.split(',')]


def simulate(nums, end_turn):
    recent_moves = {n: idx for idx, n in enumerate(nums)}
    last_spoken = 0
    turn_number = len(nums)
    while turn_number <= end_turn:
        if last_spoken in recent_moves:
            prev_turn = recent_moves[last_spoken]
            recent_moves[last_spoken] = turn_number
            last_spoken = turn_number - prev_turn
        else:
            recent_moves[last_spoken] = turn_number
            last_spoken = 0

        turn_number += 1

    return last_spoken

    


print('Part 1.', simulate(nums, 2020 - 2))
print('Part 2.', simulate(nums, 30000000 - 2))