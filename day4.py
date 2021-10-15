def part1(input):
    credential = {}
    valid = 0
    for line in input:
        line = line.strip()
        if not line: # the line is empty
            line_valid = all([key in credential for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
            if line_valid:
                valid += 1
            credential = {}
        else:
            fields = line.split()
            for field in fields:
                key, value = field.split(':')
                credential[key] = value

    return valid

def part2(input):
    credential = {}
    valid = 0
    for line in input:
        line = line.strip()
        if not line: # the line is empty
            line_valid = all([key in credential for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])
            line_valid = line_valid and is_valid(credential)
            if line_valid:
                valid += 1
            credential = {}
        else:
            fields = line.split()
            for field in fields:
                key, value = field.split(':')
                credential[key] = value

    return valid

def is_valid(credential):
    if not 1920 <= int(credential['byr']) <= 2002:
        return False
    if not 2010 <= int(credential['iyr']) <= 2020:
        return False
    if not 2020 <= int(credential['eyr']) <= 2030:
        return False
    
    height = credential['hgt']
    if height.endswith('cm'):
        if not 150 <= int(height[:-2]) <= 193:
            return False
    elif height.endswith('in'):
        if not 59 <= int(height[:-2]) <= 76:
            return False
    else:
        return False

    hair = credential['hcl']
    if not hair[0] == '#':
        return False
    if not all([c in '1234567890abcdef' for c in hair[1:]]): # for every character in the hair color, that character is in the set
        return False
    
    eye = credential['ecl']
    if eye not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    passportId = credential['pid']
    if not (len(passportId) == 9 or all([c in passportId for c in '1234567890'])):
        return False
    
    return True

if __name__ == "__main__":
    with open('day4-data.txt') as f:
        input = f.readlines()
        input.append('')

        print(part1(input))
        print(part2(input))