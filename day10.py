import itertools

def part1(input):
    ones = 0
    threes = 0
    for left, right in itertools.pairwise(input):
        if right - left == 1:
            ones += 1
        elif right - left == 3:
            threes += 1
    return ones * threes
                

def part2(input):
    return get_poss(0, input, {})

def get_poss(curr, input, curr_poss):
    if curr == len(input) - 1:
        return 1
    if curr in curr_poss:
        return curr_poss[curr]
    
    poss = 0
    for next in range(curr + 1, len(input)):
        if input[next] - input[curr] <= 3:
            poss += get_poss(next, input, curr_poss)
    
    curr_poss[curr] = poss
    return poss


if __name__ == "__main__":
    with open('day10-data.txt') as f:
        input = [
            int(line)
            for line in f.read().splitlines()
        ]

        input.append(0)
        input = sorted(input)
        input.append(input[-1] + 3)

        print(part1(input))
        print(part2(input))