with open('inputs/inp19.txt') as f:
    inp = f.read()

import re

inp = '''
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'''

rules_blob, messages_blob = inp.strip().split('\n\n')

rules = {}
rule_re = re.compile(r'^(?P<rule_id>\d+): (?P<rule_content>.*)$')


def match_rule(rule_id: int, rules: dict, message: str) -> bool:
    rule = rules[rule_id]

    if rule == 'a' or rule == 'b':
        return message[0] == rule

    return False


for rule_str in rules_blob.split('\n'):
    m = rule_re.match(rule_str)
    rule_id = int(m.group('rule_id'))
    rule_content = m.group('rule_content')

    if rule_content in {'"a"', '"b"'}:
        rules[rule_id] = rule_content.replace('"', '')
        continue

    rules[rule_id] = []
    for rule_seq in rule_content.split(' | '):
        rules[rule_id].append(list(int(rid) for rid in rule_seq.split(' ')))


c = 0
for message in messages_blob.split('\n'):
    if match_rule(0, rules, message):
        c += 1

print('Part 1.', c)