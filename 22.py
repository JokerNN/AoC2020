with open('inputs/inp22.txt') as f:
    inp = f.read()
    
# inp = '''
# Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10
# '''


def game1(deck1: list, deck2: list) -> list:
    while len(deck1) > 0 and len(deck2) > 0:
        c1, c2 = deck1.pop(0), deck2.pop(0)
        if c1 > c2:
            deck1.extend((c1, c2))
        else:
            deck2.extend((c2, c1))


    winning_deck = deck1 if len(deck1) != 0 else deck2
    return winning_deck


def calc_score(deck: list) -> int:
    s = 0
    for idx, card in enumerate(reversed(deck), start=1):
        s += idx * card

    return s


players = inp.strip().split('\n\n')
deck1 = [int(c) for c in players[0].split('\n')[1:]]
deck2 = [int(c) for c in players[1].split('\n')[1:]]


winning_deck = game1(deck1, deck2)

print('Part 1', calc_score(winning_deck))

def game_hash(deck1: list, deck2: list) -> str:
    return '_'.join(str(c) for c in deck1) + '__' + '_'.join(str(c) for c in deck2)




def game2(deck1: list, deck2: list, game_id: int=0) -> tuple:
    # print('Starting', game_id)
    prev_rounds = set()

    while len(deck1) > 0 and len(deck2) > 0:
        h = game_hash(deck1, deck2)

        if h in prev_rounds:
            return deck1, True
        else:
            prev_rounds.add(h)

        c1, c2 = deck1.pop(0), deck2.pop(0)

        if c1 <= len(deck1) and c2 <= len(deck2):
            _, p1won = game2(deck1[:c1], deck2[:c2], game_id + 1)

            if p1won:
                deck1.extend((c1, c2))
            else:
                deck2.extend((c2, c1))

        elif c1 > c2:
            deck1.extend((c1, c2))
        else:
            deck2.extend((c2, c1))


    winning_deck = deck1 if len(deck1) != 0 else deck2
    p1won = len(deck1) > 0
    return winning_deck, p1won


players = inp.strip().split('\n\n')
deck1 = [int(c) for c in players[0].split('\n')[1:]]
deck2 = [int(c) for c in players[1].split('\n')[1:]]

winning_deck, _ = game2(deck1, deck2)
print('Part 2', calc_score(winning_deck))