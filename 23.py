from typing import Optional, NewType

inp = '327465189'
# inp = '389125467'

inp = [int(c) for c in inp]


class SListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: SListNodeT = None

    def __repr__(self):
        return str(self.val)


SListNodeT = NewType('SListNodeT', Optional[SListNode])

def slice_n(node: SListNode, n: int=10):
    res = []

    for _ in range(n):
        res.append(node.val)
        node = node.next

    return res

def print_n(node: SListNode, n: int=10):
    sl = slice_n(node, n)
    print(' '.join(str(v) for v in sl))

def find_n(node: SListNode, val: int, n: int=3):
    for _ in range(n):
        if node.val == val:
            return True
        node = node.next

    return False

first = SListNode(inp[0])
node = first
for idx in inp[1:]:
    node.next = SListNode(idx)
    node = node.next

node.next = first
cur_node = first


for _ in range(100):
    cur_val = cur_node.val
    dest_val = cur_val - 1 if cur_val > 1 else 9
    pick_up = cur_node.next

    for _ in range(3):
        if find_n(pick_up, dest_val, 3):
            dest_val = dest_val -1 if dest_val > 1 else 9

    cur_node.next = cur_node.next.next.next.next

    node = cur_node
    while node.val != dest_val:
        node = node.next

    bu_next = node.next
    node.next = pick_up
    pick_up.next.next.next = bu_next

    cur_node = cur_node.next
    # print_n(first, 9)

cur_node = first
while cur_node.val != 1:
    cur_node = cur_node.next

print('Part 1', ''.join(str(v) for v in slice_n(cur_node.next, 8)))


first = SListNode(inp[0])
node = first

nodes_dict = {}
nodes_dict[inp[0]] = first

for idx in inp[1:]:
    node.next = SListNode(idx)
    node = node.next
    nodes_dict[idx] = node

for idx in range(10, 1000001):
    node.next = SListNode(idx)
    node = node.next
    nodes_dict[idx] = node

node.next = first
cur_node = first


for _ in range(10000000):
    if _ % 100000 == 0:
        print(_)

    cur_val = cur_node.val
    dest_val = cur_val - 1 if cur_val > 1 else 1000000
    pick_up = cur_node.next

    for _ in range(3):
        if find_n(pick_up, dest_val, 3):
            dest_val = dest_val -1 if dest_val > 1 else 1000000

    cur_node.next = cur_node.next.next.next.next

    node = nodes_dict[dest_val]

    bu_next = node.next
    node.next = pick_up
    pick_up.next.next.next = bu_next

    cur_node = cur_node.next

node = first
while node.val != 1:
    node = node.next

print("Part 2", node.next.val * node.next.next.val)