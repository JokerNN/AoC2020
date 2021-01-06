from collections import defaultdict, namedtuple
from typing import Dict, List, Optional, Generator, Set
from math import sqrt

with open('inputs/inp20.txt') as f:
    inp = f.read()


def rotate_pic_left(pic: List[str]) -> List[str]:
    new_pic = ['' for _ in range(len(pic))]
    for row in pic:
        for c_idx, char in enumerate(reversed(row)):
            new_pic[c_idx] += char

    return new_pic

def reflect_pic(pic: List[str], direction: str) -> List[str]:
    if direction == 'hr':
        return [''.join(reversed(row)) for row in pic]
    elif direction == 'vr':
        return list(reversed(pic))
    else:
        raise Exception("Unknown direction", direction)


class Tile:
    def __init__(self, tile_id: int, pic: List[str]):
        self.pic = pic
        self.id = tile_id
        self.__init_ids()

    def __init_ids(self) -> None:
        self.top_id = self.pic[0]
        self.bottom_id = self.pic[-1]
        self.left_id = ''.join(r[0] for r in self.pic)
        self.right_id = ''.join(r[-1] for r in self.pic)

    def __repr__(self) -> str:
        pic = '\n'.join(self.pic)
        return f'{self.id}\n{pic}\n'

    def get_all_ids(self) -> Generator[str, None, None]:
        yield self.top_id
        yield self.right_id
        yield self.bottom_id
        yield self.left_id

    def rotate_left(self) -> None:
        self.pic = rotate_pic_left(self.pic)
        self.__init_ids()

    def reflect(self, direction: str) -> None:
        self.pic = reflect_pic(self.pic, direction)

        self.__init_ids()

Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])

def get_neighbours(point: Point) -> Dict[str, Point]:
    return {
        'top': Point(point.x, point.y - 1),
        'right': Point(point.x + 1, point.y),
        'bottom': Point(point.x, point.y + 1),
        'left': Point(point.x - 1, point.y)
    }

def print_pic(pic: List[str]) -> str:
    return '\n'.join(''.join(row) for row in pic)

def match_pattern(pattern: List[str], pic: List[str], tl_pos: Point) -> Optional[set]:
    match_set = set()
    for y in range(len(pattern)):
        for x in range(len(pattern[y])):
            pattern_symbol = pattern[y][x]
            pic_point = Point(tl_pos.x + x, tl_pos.y + y)
            try:
                if pattern_symbol == '#' and pic[pic_point.y][pic_point.x] == '#':
                    match_set.add(pic_point)
                elif pattern_symbol == '#' and pic[pic_point.y][pic_point.x] != '#':
                    return None
            except IndexError:
                return None

    return match_set
            


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
side_len = int(sqrt(len(tiles)))


#orient corner to be top left
for __ in range(4):
    if (borders[first_tile.right_id] == 2 or borders[first_tile.right_id[::-1]] == 2)\
            and (borders[first_tile.bottom_id] == 2 or borders[first_tile.bottom_id[::-1]]):
        # orientation_found = True
        break

    first_tile.rotate_left()


class TileFoundException(Exception):
    pass


for step in range(1, 2 * side_len - 1):
    empty_spaces = []

    for i in range(0, step + 1):
        if i < side_len and step - i < side_len:
            empty_spaces.append(Point(i, step - i))

    # print(empty_spaces)


    # print(empty_spaces)
    for space in empty_spaces:
        lb = None
        tb = None
        l_neighbour = Point(space.x - 1, space.y)
        t_neighbour = Point(space.x, space.y - 1)
        if l_neighbour in grid:
            lb = tiles[grid[l_neighbour]].right_id
        if t_neighbour in grid:
            tb = tiles[grid[t_neighbour]].bottom_id
        try: 
            for tile in tiles.values():
                if tile.id in used_tiles:
                    continue

                for _ in range(4):
                    if lb in {tile.left_id, None} and tb in {tile.top_id, None}:
                        # tile found
                        grid[space] = tile.id
                        used_tiles.add(tile.id)
                        raise TileFoundException
                    else:
                        tile.rotate_left()

                tile.reflect('vr')

                for _ in range(4):
                    if lb in {tile.left_id, None} and tb in {tile.top_id, None}:
                        # tile found
                        grid[space] = tile.id
                        used_tiles.add(tile.id)
                        raise TileFoundException
                    else:
                        tile.rotate_left()
            else:
                raise Exception("Tile not found")

        except TileFoundException:
            continue
                

print(grid[Point(side_len - 1, side_len - 1)])


# restore full picture

pic: List[str] = []
for y in range(side_len):
    for r_idx in range(len(first_tile.top_id) - 2):
        row = ''
        for x in range(side_len):
            tile_id = grid[Point(x, y)]
            chars = tiles[tile_id].pic[r_idx + 1]
            row += (chars[1: -1])

        pic.append(row)
        

print(print_pic(pic))
# pic = rotate_pic_left(pic)

monster_pattern = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''

monster_pattern = monster_pattern.split('\n')

monster_cells: Set[Point, ] = set()

for _ in range(2):
    if len(monster_cells) > 0:
        break

    for _ in range(4):
        if len(monster_cells) > 0:
            break

        for y in range(len(pic)):
            row = pic[y]
            for x in range(len(row)):
                m = match_pattern(monster_pattern, pic, Point(x, y))
                if m:
                    monster_cells.update(m)

        pic = rotate_pic_left(pic)


    pic = reflect_pic(pic, 'vr')

    

water_roughness = 0
for y in range(len(pic)):
    row = pic[y]
    for x in range(len(row)):
        if pic[y][x] == '#':
            water_roughness += 1


print('Part 2', water_roughness - len(monster_cells))