def part1(input):
    for i in input:
        for j in input:
            if i + j == 2020:
                return i * j

def part2(input):
    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    return i * j * k

if __name__ == "__main__":
    with open('day1-data.txt') as f:
        inputs = [
            int(line)
            for line in f.read().splitlines()
        ]
        print(part1(inputs))
        print(part2(inputs))