f = open('inputs/inp4.txt', 'r')
import re

inp = f.read()
passes = inp.split('\n\n')

required_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid'
}

valid_count = 0
for p in passes:
    fields = re.split(' |\n', p)
    # print(fields)
    field_types = {f.split(':')[0] for f in fields}
    field_types.discard('cid')

    if field_types == required_fields:
        valid_count += 1

print("Part 1.", valid_count)

def validate_year(min, max):
    def validate(year):
        if re.match(r'\d{4}$', year):
            y = int(year)
            return min <= y <= max
        return False

    return validate

def validate_height(h):
    if re.match(r'\d{3}cm$', h):
        _h = int(h[:3])
        return 150 <= _h <= 193
    if re.match(r'\d{2}in$', h):
        _h = int(h[:2])
        return 59 <= _h <= 76

    return False

def validate_hcl(color):
    return bool(re.match(r'#[a-f0-9]{6}$', color))

def validate_ecl(color):
    return color in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def validate_pid(pid):
    return bool(re.match(r'\d{9}$', pid))

def validate_cid(cid):
    return True

def validate_field(f_type, value):
    validators = {
        'byr': validate_year(1920, 2002),
        'iyr': validate_year(2010, 2020),
        'eyr': validate_year(2020, 2030),
        'hgt': validate_height,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid,
        'cid': validate_cid
    }
    
    return validators[f_type](value)

valid_count = 0
for p in passes:
    fields = re.split(' |\n', p)
    # print(fields)
    field_types = {f.split(':')[0] for f in fields}
    field_types.discard('cid')

    if field_types == required_fields:
        for f in fields:
            f_type, f_value = f.split(':')
            if not validate_field(f_type, f_value):
                break
        else:
            valid_count += 1

print("Part 2.", valid_count)