from collections import defaultdict, namedtuple
# from copy import copy

with open('inputs/inp24.txt') as f:
    inp = f.read()

# inp = '''
# sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew
# '''


Point = namedtuple('Point', ['x', 'y', 'z'], defaults=[0, 0, 0])

dirs = {
    'e': Point(1, -1, 0), 
    'se': Point(0, -1, 1), 
    'sw': Point(-1, 0, 1), 
    'w': Point(-1, 1, 0), 
    'nw': Point(0, 1, -1), 
    'ne': Point(1, 0, -1)
}

def traverse_and_flip(grid: defaultdict, root: Point, path: str) -> None:
    x, y, z= root.x, root.y, root.z
    while path != '':
        if path[0] in dirs:
            d = path[0]
            path = path[1:]
        else:
            d = path[:2]
            path = path[2:]

        if d not in dirs:
            raise Exception('No such dir', d)

        x += dirs[d].x
        y += dirs[d].y
        z += dirs[d].z

    p = Point(x, y, z)
    grid[p] = 'white' if grid[p] == 'black' else 'black'

def count_color(grid: defaultdict, color: str) -> int:
    c = 0
    for tile in grid.values():
        if tile == 'black':
            c += 1

    return c
        

grid = defaultdict(lambda: 'white')

for line in inp.strip().split('\n'):
    traverse_and_flip(grid, Point(0, 0, 0), line)


print('Part 1', count_color(grid, 'black'))


def cycle(grid: defaultdict) -> None:
    mutations = []
    for point in list(grid.keys()):
        bc = 0
        for d in dirs.values():
            np = Point(point.x + d.x, point.y + d.y, point.z + d.z)
            if grid[np] == 'black':
                bc += 1

        color = grid[point]

        if color == 'black' and (bc == 0 or bc > 2):
            mutations.append(point)
        elif color == 'white' and bc == 2:
            mutations.append(point)

    for p in mutations:
        grid[p] = 'black' if grid[p] == 'white' else 'white'


for point in list(grid.keys()):
    bc = 0
    for d in dirs.values():
        np = Point(point.x + d.x, point.y + d.y, point.z + d.z)
        grid[np]

for _ in range(100):
    # print(_, count_color(grid, 'black'))
    cycle(grid)

print('Part 2', count_color(grid, 'black'))