from collections import defaultdict

def part1(input):
    result = -1
    for bpass in input:
        seat_id = get_seat_id(bpass)
        if seat_id > result:
            result = seat_id
    return result

def part2(input):
    result = set()
    for bpass in input:
        result.add(get_seat_id(bpass))

    for seat_id in sorted(result):
        if seat_id+1 not in result and seat_id+2 in result:
            return seat_id+1

def get_seat_id(bpass):
    row_assignment = bpass[:7]
    col_assignment = bpass[7:]

    row_assignment = row_assignment.replace('F', '0')
    row_assignment = row_assignment.replace('B', '1')
    row = int(row_assignment, 2)

    col_assignment = col_assignment.replace('L', '0')
    col_assignment = col_assignment.replace('R', '1')
    col = int(col_assignment, 2)

    return row * 8 + col

if __name__ == "__main__":
    with open('day5-data.txt') as f:
        input = f.readlines()

        print(part1(input))
        print(part2(input))