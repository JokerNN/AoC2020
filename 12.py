from collections import namedtuple

with open('./inp12.txt') as f:
    inp = f.read()

# inp = '''F10
# N3
# F7
# R90
# F11
# '''


instructions = inp.strip().split('\n')

Point = namedtuple('Point', ['x', 'y'])

dir_vecs = {
    'N': Point( 0,  1),
    'S': Point( 0, -1),
    'E': Point( 1,  0),
    'W': Point(-1,  0)
}

turns = ['N', 'E', 'S', 'W']

def turn(cur_dir, turn_dir, degree):
    if turn_dir == 'L':
        step = -1
    elif turn_dir == 'R':
        step = 1
    else:
        raise Exception('Unknown turn dir', turn_dir)

    for _ in range(degree // 90):
        new_index = (turns.index(cur_dir) + step) % len(turns)
        cur_dir = turns[new_index]

    return cur_dir
     

def process_instruction(pos, direction, ins, param):
    if ins == 'F':
        ins = direction
    
    if ins in {'L', 'R'}:
        direction = turn(direction, ins, param)
    elif ins in {'N', 'W', 'S', 'E'}:
        pos = Point(pos.x + dir_vecs[ins].x * param, pos.y + dir_vecs[ins].y * param)
    else:
        raise Exception('Unknown instruction', ins)

    return pos, direction

def turn_waypoint(waypoint, turn_dir, degree):
    
    if turn_dir not in {'L', 'R'}:
        raise Exception('Unknown turn dir', turn_dir)

    for _ in range(degree // 90):
        if turn_dir == 'L':
            waypoint = Point(-waypoint.y, waypoint.x)
        elif turn_dir == 'R':
            waypoint = Point(waypoint.y, -waypoint.x)

    return waypoint



def process_instruction2(pos, waypoint, ins, param):
    if ins in {'L', 'R'}:
        waypoint = turn_waypoint(waypoint, ins, param)
    elif ins in {'N', 'W', 'S', 'E'}:
        waypoint = Point(waypoint.x + dir_vecs[ins].x * param, waypoint.y + dir_vecs[ins].y * param)
    elif ins == 'F':
        pos = Point(pos.x + waypoint.x * param, pos.y + waypoint.y * param)
    else:
        raise Exception('Unknown instruction', ins)

    return pos, waypoint



pos = Point(0, 0)
direction = 'E'

for ins_line in instructions:
    ins = ins_line[:1]
    param = int(ins_line[1:])
    pos, direction = process_instruction(pos, direction, ins, param)

print(pos, direction)
    
print('Part 1.', abs(pos.x) + abs(pos.y))

pos = Point(0, 0)
waypoint = Point(10, 1)

for ins_line in instructions:
    ins = ins_line[:1]
    param = int(ins_line[1:])
    pos, waypoint = process_instruction2(pos, waypoint, ins, param)

print('Part 2.', abs(pos.x) + abs(pos.y))