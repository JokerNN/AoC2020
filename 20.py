from collections import defaultdict, namedtuple
from typing import Dict, List, Optional, Generator
from math import sqrt

with open('inputs/inp20.txt') as f:
    inp = f.read()

# inp = '''
# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###

# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..

# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...

# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.

# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..

# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.

# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#

# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.

# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###...
# '''

class Tile:
    def __init__(self, tile_id: int, pic: List[str]):
        self.pic = pic
        self.id = tile_id
        self.top_id = pic[0]
        self.bottom_id = pic[-1]
        self.left_id = ''.join(r[0] for r in pic)
        self.right_id = ''.join(r[-1] for r in pic)

    def __repr__(self) -> str:
        pic = '\n'.join(self.pic)
        return f'{self.id}\n{pic}\n'

    def get_all_ids(self) -> Generator[str, None, None]:
        yield self.top_id
        yield self.right_id
        yield self.bottom_id
        yield self.left_id

Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])

def get_neighbours(point: Point) -> Dict[str, Point]:
    return {
        'top': Point(point.x, point.y - 1),
        'right': Point(point.x + 1, point.y),
        'bottom': Point(point.x, point.y + 1),
        'left': Point(point.x - 1, point.y)
    }

def find_tile(tiles: dict, target_border: str, used_tiles: set) -> Optional[Tile]:
    for tile in tiles.values():
        if tile.id in used_tiles:
            continue

        if tile.top_id == target_border or tile.top_id[::-1] == target_border\
            or tile.right_id == target_border or tile.right_id[::-1] == target_border\
            or tile.bottom_id == target_border or tile.bottom_id[::-1] == target_border\
            or tile.left_id == target_border or tile.left_id[::-1] == target_border:
                return tile

    return None

tiles = {}

for tile_str in inp.strip().split('\n\n'):
    tile_rows = tile_str.split('\n')
    tile_head = tile_rows[0]
    tile_id = int(tile_head[5:-1])
    tiles[tile_id] = Tile(tile_id, tile_rows[1:])



borders = defaultdict(int)
for tile in tiles.values():
    for b_id in tile.get_all_ids():
        rev = b_id[::-1]
        if rev in borders:
            borders[rev] += 1
        else:
            borders[b_id] += 1

corner_tiles = []
for tile in tiles.values():
    uniq_count = 0
    for b_id in tile.get_all_ids():
        if borders[b_id] == 1:
            uniq_count += 1

    if uniq_count > 1:
        corner_tiles.append(tile)


p = 1
for t in corner_tiles:
    p *= t.id

print('Part 1', p)


used_tiles = set()
grid = {}
first_tile = corner_tiles[0]
grid[Point(0, 0)] = first_tile.id
used_tiles = set([first_tile.id])

#all borders are either unique or match to only one another border
while len(used_tiles) < len(tiles):
    empty_spaces = []
    for point, tile in grid.items():
        for direction, neigbour in get_neighbours(point).items():
            if neigbour not in grid:
                empty_spaces.append(neigbour)
    
    # print(empty_spaces)
    for space in empty_spaces:
        for direction, neigbour in get_neighbours(space).items():
            if neigbour in grid:
                n_tile = tiles[grid[neigbour]]
                tile = find_tile(tiles, n_tile.top_id, used_tiles)
                if not tile:
                    tile = find_tile(tiles, n_tile.right_id, used_tiles)
                if not tile:
                    tile = find_tile(tiles, n_tile.bottom_id, used_tiles)
                if not tile:
                    tile = find_tile(tiles, n_tile.left_id, used_tiles)
                
                if tile:
                    grid[space] = tile.id
                    used_tiles.add(tile.id)
                        


print(grid)