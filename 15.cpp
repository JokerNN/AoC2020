/**
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
    */
#include <iostream>
#include <unordered_map>

using namespace std;

typedef unordered_map<unsigned int, unsigned int> intmap;

int simulate(unsigned int *nums, unsigned int nums_size, unsigned int end_turn) {
    intmap recent_moves;
    // int recent_moves[recent_moves_size];
    // for (int i = 0; i < recent_moves_size; ++i) {
    //     recent_moves[i] = -1;
    // }
    int last_spoken = 0;
    unsigned int turn_number = nums_size;
    for (unsigned int i = 0; i < nums_size; ++i) {
        unsigned int num = nums[i];
        recent_moves[num] = i;
    }
    while (turn_number <= end_turn) {
        intmap::const_iterator prev_turn_it = recent_moves.find(last_spoken);
        if (prev_turn_it != recent_moves.end()) {
            unsigned int prev_turn = prev_turn_it->second;
            recent_moves[last_spoken] = turn_number;
            last_spoken = turn_number - prev_turn;
        } else {
            recent_moves[last_spoken] = turn_number;
            last_spoken = 0;
        }
        turn_number++;
    }

    return last_spoken;
}

int main() {
    unsigned int nums[] = {2, 20, 0, 4, 1, 17};
    unsigned int nums_size = 6;

    cout << "Part 1. " << simulate(nums, nums_size, 2020 - 2) << endl;
    cout << "Part 2. " << simulate(nums, nums_size, 30000000 - 2) << endl;
}