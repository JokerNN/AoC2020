from typing import List, Dict


with open('inputs/inp19.txt') as f:
    inp = f.read()

# inp = '''
# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb
# '''


def match(message: str, rule_stack: "List[int | str]", rules: "Dict[int, List[List[int]] | str]") -> bool:
    if len(rule_stack) > len(message):
        return False
    elif len(rule_stack) == 0 or len(message) == 0:
        return len(rule_stack) == len(message) == 0

    r = rule_stack.pop(0)
    if isinstance(r, str):
        if message[0] == r:
            return match(message[1:], list(rule_stack), rules)
    else:
        for rule in rules[r]:
            if match(message, list(rule) + rule_stack, rules):
                return True

    return False


rules_inp, messages_inp = inp.strip().split('\n\n')
messages = messages_inp.strip().split('\n')


rules = {}
for rule_str in rules_inp.strip().split('\n'):
    r_id, content = rule_str.split(': ')
    r_id = int(r_id)
    
    if content[0] == '"':
        rules[r_id] = content[1]
    else:
        rule_parts = content.split(' | ')
        rules[r_id] = []
        for part in rule_parts:
            rules[r_id].append([int(n) for n in part.split(' ')])

mc = 0
for message in messages:
    if match(message, list(rules[0][0]), rules):
        mc += 1

print("Part 1.", mc)

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

mc = 0
for message in messages:
    if match(message, list(rules[0][0]), rules):
        mc += 1

print("Part 2.", mc)