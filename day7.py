from collections import defaultdict

rules = defaultdict(str)
contains = defaultdict(str)

def part1(input):
    for rule in input:
        (container, containees) = rule.split(' contain ')
        last_space = container.rindex(' ')
        container = container[:last_space]
        if containees == 'no other bags.':
            continue
        elif containees.count(',') == 0:
            last_space = containees.rindex(' ')
            contains.setdefault(containees[2:last_space], []).append(container)
        else:
            containeesArr = containees[:-1].split(', ')
            for containee in containeesArr:
                last_space = containee.rindex(' ')
                contains.setdefault(containee[2:last_space], []).append(container)
    return len(can_contain('shiny gold'))


def part2(input):
    for rule in input:
        (container, containees) = rule.split(' contain ')
        last_space = container.rindex(' ')
        container = container[:last_space]
        if containees == 'no other bags.':
            continue
        elif containees.count(',') == 0:
            last_space = containees.rindex(' ')
            rules.setdefault(container, []).append(containees[:last_space])
        else:
            containeesArr = containees[:-1].split(', ')
            for containee in containeesArr:
                last_space = containee.rindex(' ')
                rules.setdefault(container, []).append(containee[:last_space])
    return count_bags('shiny gold')

def can_contain(color):
    count = set(contains[color])
    containers = contains[color]
    for container in containers:
        count = count | can_contain(container)
    return count

def count_bags(color):
    result = 0
    for containee in rules[color]:
        (numStr, sub_color) = containee.split(' ', 1)
        num = int(numStr)
        result = result + num + (num * count_bags(sub_color))
    return result

if __name__ == "__main__":
    with open('day7-data.txt') as f:
        input = f.read().splitlines()

        print(part1(input))
        print(part2(input))