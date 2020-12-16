import re
from collections import namedtuple
from itertools import permutations

with open('inp16.txt') as f:
    inp = f.read()

# inp = '''
# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# '''

# inp = '''
# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
# '''

Rule = namedtuple('Rule', ['name', 'range1', 'range2'])

def match_rule(rule: Rule, value: int) -> bool:
    range1, range2 = rule.range1, rule.range2
    return value >= range1[0] and value <= range1[1] or value >= range2[0] and value <= range2[1]


inp_format = re.compile(
r'''(?P<rules>.*)

your ticket:
(?P<my_ticket>[\d,]+)

nearby tickets:
(?P<tickets>.*)
''', re.MULTILINE | re.DOTALL)

m = inp_format.match(inp)

rules_txt = m.group('rules')
my_ticket_txt = m.group('my_ticket')
tickets = m.group('tickets')

rules = {}
rule_re = re.compile(r'(?P<name>.*): (?P<rule1_start>\d+)-(?P<rule1_end>\d+) or (?P<rule2_start>\d+)-(?P<rule2_end>\d+)')

for rule in rules_txt.strip().split('\n'):
    m = rule_re.match(rule)
    range1 = (int(m.group('rule1_start')), int(m.group('rule1_end')))
    range2 = (int(m.group('rule2_start')), int(m.group('rule2_end')))
    rule = Rule(m.group('name'), range1, range2)
    rules[rule.name] = rule

s = 0

filtered_tickets = []
for ticket in tickets.strip().split('\n'):
    values = [int(t) for t in ticket.split(',')]
    for value in values:
        for rule in rules.values():
            if match_rule(rule, value):
                break

        else:
            s += value
            break
    else:
        filtered_tickets.append(values)
            

print('Part 1.', s)

field_assignments = {
    idx: set(rules.keys()) for idx in range(len(filtered_tickets[0]))
}


for ticket in filtered_tickets:
    for idx, val in enumerate(ticket):
        for rule in rules.values():
            if not match_rule(rule, val):
                field_assignments[idx].discard(rule.name)


def count_rule_occurences(rule_name: str, assignments: dict):
    count = 0
    for item in assignments.values():
        if rule_name in item:
            count += 1

    return count

for _ in range(20):
    for rule_name in rules.keys():
        count = count_rule_occurences(rule_name, field_assignments)
        if count == 1:
            for idx, s in field_assignments.items():
                if rule_name in s:
                    field_assignments[idx] = {rule_name}

# print(field_assignments)

my_ticket = [int(t) for t in my_ticket_txt.strip().split(',')]
p = 1
for idx, field in field_assignments.items():
    field_name = field.pop()
    if field_name.startswith('departure'):
        p *= my_ticket[idx]

print('Part 2.', p)

        