def part1(input):
    return get_trees(input, 1, 3)

def part2(input):
    return (
        get_trees(input, 1, 1) *
        get_trees(input, 1, 3) *
        get_trees(input, 1, 5) *
        get_trees(input, 1, 7) *
        get_trees(input, 2, 1)
    )

def get_trees(input, row_rate, col_rate):
    #starting at 0,0 move right col_rate down row_rate and count # chars
    #wrap the input
    row, col = 0, 0
    trees = 0
    while row < len(input):
        if input[row][col] == '#':
            trees+=1
        row+=row_rate
        col+=col_rate
        col%=len(input[0])
    return trees

if __name__ == "__main__":
    with open('day3-data.txt') as f:
        input = []
        for line in f.read().splitlines():
            input.append(line)

        print(part1(input))
        print(part2(input))