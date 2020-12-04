import sys
import re

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
validators = {
    'byr': (lambda x: True if 1920 <= int(x) <= 2002 else False),
    'iyr': (lambda x: True if 2010 <= int(x) <= 2020 else False),
    'eyr': (lambda x: True if 2020 <= int(x) <= 2030 else False),
    'hgt': (lambda x: True if ((x[-2:]=='cm' and 150 <= int(x[:-2]) <= 193) or
        (x[-2:]=='in' and 59 <= int(x[:-2]) <= 76)) else False),
    'hcl': re.compile('^#[0-9a-f]{6}$'),
    'ecl': re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$'),
    'pid': re.compile('^\d{9}$'),
}

def validate(passport):
    for key, value in passport.items():
        if key in {'byr', 'iyr', 'eyr', 'hgt'}: 
            if not validators[key](value): return False
        elif key in {'hcl', 'ecl', 'pid'}:
            if validators[key].search(value) is None: return False
    return True 


if __name__ == '__main__':
    input_file = sys.argv[1]
    data = [{key: value for key, value in (
        pair.split(':') for pair in re.split('\n| ', passport))}
        for passport in open(input_file).read().rstrip().split("\n\n")]

    present, valid = 0, 0 
    for passport in data:
        if len(required.intersection(passport.keys())) == 7:
            present += 1
            if validate(passport): valid += 1
    print(f"{present}, {valid}")
