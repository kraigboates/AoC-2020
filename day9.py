def part1(input, preamble_size = 25):
    for idx, candidate in enumerate(input):
        if idx >= preamble_size:
            found = False
            possibilities = input[idx-preamble_size:idx]
            for poss1 in possibilities:
                for poss2 in possibilities:
                    if poss1 == poss2:
                        continue
                    elif poss1 + poss2 == candidate:
                        found = True
                        break
                if found:
                    break
            if not found:
                return candidate
                

def part2(input):
    target = part1(input)
    for idx in range(len(input)):
        for length in range(len(input) - idx):
            poss = input[idx:len(input) - length]
            total = sum(poss)
            if total == target:
                return min(poss) + max(poss)

if __name__ == "__main__":
    with open('day9-data.txt') as f:
        input = [
            int(line)
            for line in f.read().splitlines()
        ]

        print(part1(input))
        print(part2(input))