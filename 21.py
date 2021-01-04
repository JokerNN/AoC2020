import re
from collections import defaultdict

with open('inputs/inp21.txt') as f:
    inp = f.read()

# inp = '''
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)
# '''

allergen_re = re.compile(r'^(?P<ing>.*) \(contains (?P<all>.*)\)$')

allergen_map = defaultdict(set)

for ing_line in inp.strip().split('\n'):
    m = allergen_re.match(ing_line)
    ings = m.group('ing').split(' ')
    allergens = m.group('all').split(', ')
    for ing in ings:
        allergen_map[ing].update(set(allergens))

