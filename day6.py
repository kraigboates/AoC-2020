def part1(input):
    group = set()
    claims_total = 0
    for line in input:
        line = line.strip()
        if not line: # the line is empty
            claims_total += len(group)
            group = set()
        else:
            for char in line:
                group.add(char)

    return claims_total


def part2(input):
    group = set()
    initial = True
    claims_total = 0
    for line in input:
        line = line.strip()
        if not line: # the line is empty
            claims_total += len(group)
            group = set()
            initial = True
        else:
            if initial:
                for char in line:
                    group.add(char)
                initial = False
            else:
                test = set()
                for char in line:
                    test.add(char)
                group = group & test

    return claims_total



if __name__ == "__main__":
    with open('day6-data.txt') as f:
        input = f.readlines()
        input.append('')

        print(part1(input))
        print(part2(input))