def part1(input):
    valid = 0
    for line in input:
        [limits, character, password] = line.split(' ')
        lower, upper = map(int, limits.split('-'))
        character = character[0]
        occurrences = password.count(character)
        if lower <= occurrences <= upper:
            valid+=1
    return valid

def part2(input):
    valid = 0
    for line in input:
        [positions, character, password] = line.split(' ')
        first, second = map(int, positions.split('-'))
        first-=1 # password indexes start at 1
        second-=1
        character = character[0]
        firstMatches = password[first] == character
        secondMatches = password[second] == character
        if firstMatches ^ secondMatches:
            valid+=1
    return valid

if __name__ == "__main__":
    with open('day2-data.txt') as f:
        inputs = f.read().splitlines()

        print(part1(inputs))
        print(part2(inputs))