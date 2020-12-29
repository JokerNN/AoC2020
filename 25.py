card_pk = 19241437
door_pk = 17346587

def find_loop_size(pk: int) -> int:
    sub = 7
    val = 1
    loops = 0
    while val != pk:
        val *= sub
        val %= 20201227
        loops += 1

    return loops

def find_pk(sub: int, loop_size: int) -> int:
    val = 1
    for _ in range(loop_size):
        val *= sub
        val %= 20201227

    return val

print("Finding card loop size")
card_ls = find_loop_size(card_pk)
print("Finding door loop size")
door_ls = find_loop_size(door_pk)

print("Part 1", find_pk(door_pk, card_ls))