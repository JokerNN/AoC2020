from collections import defaultdict, namedtuple

Point = namedtuple('Point', ['x', 'y', 'z', 'w'], defaults=[0, 0, 0, 0])
Mutation = namedtuple('Mutation', ['pos', 'new_value'])

with open('inputs/inp17.txt') as f:
    inp = f.read().strip()


# inp = '''
# .#.
# ..#
# ###
# '''


def slice_grid(grid: dict, top_left: Point, bottom_right: Point, coord: int):
    result = defaultdict(lambda: defaultdict(dict))

    for pos, val in grid.items():
        plist = list(pos)
        c = plist.pop(coord)
        result[c][plist[0]][plist[1]] = val

    final_result = {}

    for key in result.keys():
        res = result[key]
        min0 = min(res.keys())
        max0 = max(res.keys())
        min1 = min(res[0].keys())
        max1 = max(res[0].keys())
        coord_grid = []

        for c0 in range(min0, max0 +1):
            row = []
            for c1 in range(min1, max1 + 1):
                row.append(res[c0][c1])

            coord_grid.append(row)

        final_result[key] = '\n'.join(''.join(row) for row in coord_grid)

    return final_result

def count_active_neigbours(grid: dict, pos: Point):
    count = 0
    for x in range(pos.x - 1, pos.x + 2):
        for y in range(pos.y - 1, pos.y + 2):
            for z in range(pos.z - 1, pos.z + 2):
                if x == pos.x and y == pos.y and z == pos.z:
                    continue

                elif grid[Point(x, y, z)] == '#':
                    count += 1

    return count

def cycle(grid: dict, top_left: Point, bottom_right: Point):
    mutations = []
    for x in range(top_left.x, bottom_right.x + 1):
        for y in range(top_left.y, bottom_right.y + 1):
            for z in range(top_left.z, bottom_right.z + 1):
                p = Point(x, y, z)
                anc = count_active_neigbours(grid, p)
                if grid[p] == '#' and anc not in {2, 3}:
                    mutations.append(Mutation(p, '.'))
                elif grid[p] == '.' and anc == 3:
                    mutations.append(Mutation(p, '#'))

    for mutation in mutations:
        grid[mutation.pos] = mutation.new_value


rows = inp.strip().split('\n')
grid = defaultdict(lambda: '.')

for r_idx, row in enumerate(rows):
    for c_idx, c in enumerate(row):
        coord = Point(c_idx, r_idx, 0)
        grid[coord] = c


top_left = Point(0, 0, 0)
bottom_right = Point(len(rows[0]), len(rows), 0)

for _ in range(6):
    top_left = Point(top_left.x -1, top_left.y - 1, top_left.z - 1)
    bottom_right = Point(bottom_right.x + 1, bottom_right.y + 1, bottom_right.z + 1)
    cycle(grid, top_left, bottom_right)
    # slice_grid(grid, top_left, bottom_right, 2)

print('Part 1.', len(list(filter(lambda v: v == '#', grid.values()))))


def count_active_neigbours2(grid: dict, pos: Point):
    count = 0
    for x in range(pos.x - 1, pos.x + 2):
        for y in range(pos.y - 1, pos.y + 2):
            for z in range(pos.z - 1, pos.z + 2):
                for w in range(pos.w - 1, pos.w + 2):
                    if x == pos.x and y == pos.y and z == pos.z and pos.w == w:
                        continue

                    elif grid[Point(x, y, z, w)] == '#':
                        count += 1

    return count


def cycle2(grid: dict, top_left: Point, bottom_right: Point):
    mutations = []
    for x in range(top_left.x, bottom_right.x + 1):
        for y in range(top_left.y, bottom_right.y + 1):
            for z in range(top_left.z, bottom_right.z + 1):
                for w in range(top_left.w, bottom_right.w + 1):
                    p = Point(x, y, z, w)
                    anc = count_active_neigbours2(grid, p)
                    if grid[p] == '#' and anc not in {2, 3}:
                        mutations.append(Mutation(p, '.'))
                    elif grid[p] == '.' and anc == 3:
                        mutations.append(Mutation(p, '#'))

    for mutation in mutations:
        grid[mutation.pos] = mutation.new_value


rows = inp.strip().split('\n')
grid = defaultdict(lambda: '.')

for r_idx, row in enumerate(rows):
    for c_idx, c in enumerate(row):
        coord = Point(c_idx, r_idx, 0)
        grid[coord] = c



top_left = Point(0, 0, 0, 0)
bottom_right = Point(len(rows[0]), len(rows), 0, 0)

for _ in range(6):
    print('Cyclce', _)
    top_left = Point(top_left.x -1, top_left.y - 1, top_left.z - 1, top_left.w - 1)
    bottom_right = Point(bottom_right.x + 1, bottom_right.y + 1, bottom_right.z + 1, bottom_right.w + 1)
    cycle2(grid, top_left, bottom_right)

print('Part 1.', len(list(filter(lambda v: v == '#', grid.values()))))