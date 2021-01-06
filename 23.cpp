// for _ in range(10000000):
//     if _ % 1000000 == 0:
//         print(_)

//     cur_val = cur_node.val
//     dest_val = cur_val - 1 if cur_val > 1 else 1000000
//     pick_up = cur_node.next

//     for _ in range(3):
//         if find_n(pick_up, dest_val, 3):
//             dest_val = dest_val -1 if dest_val > 1 else 1000000

//     cur_node.next = cur_node.next.next.next.next

//     node = nodes_dict[dest_val]

//     bu_next = node.next
//     node.next = pick_up
//     pick_up.next.next.next = bu_next

//     cur_node = cur_node.next

// node = first
// while node.val != 1:
//     node = node.next

#include <iostream>
#include <array>
#include <unordered_map>

struct SListNode {
    unsigned int val;
    SListNode* next;

    SListNode (int _val) {
        this->val = _val;
    }
};

using namespace std;

typedef unordered_map<int, SListNode*> node_map;

bool find_n(SListNode* node, int val, int n) {
    for (int loop = 0; loop < 3; ++loop) {
        if (node->val == val) {
            return true;
        }
        node = node->next;
    }
    
    return false;
}

int main() {
    array<int, 9> input = {3, 2, 7, 4, 6, 5, 1, 8, 9};
    SListNode* first = new SListNode(input[0]);
    SListNode* node = first;
    auto nodes_dict = node_map(1000000);
    nodes_dict[first->val] = first;

    for (auto it = input.begin() + 1; it != input.end(); ++it) {
        node->next = new SListNode(*it);
        node = node->next;
        nodes_dict[node->val] = node;
    }

    for (int idx = 10; idx <= 1000000; ++idx) {
        node->next = new SListNode(idx);
        node = node->next;
        nodes_dict[node->val] = node;
    }

    node->next = first;

    SListNode* cur_node = first;

    for (int loop_idx = 0; loop_idx < 10000000; ++loop_idx) {
        if (loop_idx % 1000000 == 0) {
            cout << loop_idx << endl;
        }
        int cur_val = cur_node->val;
        int dest_val = cur_val - 1;
        if (dest_val == 0) {
            dest_val = 1000000;
        }
        SListNode* pick_up = cur_node->next;

        for (int pick_idx = 0; pick_idx < 3; ++pick_idx) {
            if (find_n(pick_up, dest_val, 3)) {
                dest_val -= 1;
                if (dest_val == 0) {
                    dest_val = 1000000;
                }
            }
        }

        cur_node->next = cur_node->next->next->next->next;

        node = nodes_dict.at(dest_val);

        SListNode* bu_next = node->next;
        node->next = pick_up;
        pick_up->next->next->next = bu_next;

        cur_node = cur_node->next;
    }

    auto node1 = nodes_dict.at(1);
    unsigned long long int res = (unsigned long long int)node1->next->val * (unsigned long long int)node1->next->next->val;
    cout << "Part 2. " << res << endl;

    return 0;
}