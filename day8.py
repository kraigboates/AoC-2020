from collections import defaultdict
from copy import deepcopy


def part1(input):
    accumulator = 0
    program = defaultdict(int)
    for i, instruction in enumerate(input):
        program[i] = (instruction, False)

    pos = 0
    while True:
        (instruction, visited) = program[pos]
        if visited:
            break
        else:
            program[pos] = (instruction, True)

        (operation, arg) = instruction.split()
        
        if operation == 'acc':
            accumulator += int(arg)
            pos += 1
        elif operation == 'jmp':
            pos += int(arg)
        else:
            pos += 1
    return accumulator


def part2(input):
    program = defaultdict(int)
    for i, instruction in enumerate(input):
        program[i] = (instruction, False)

    for line in range(len(program)):
        new_program = deepcopy(program)
        (instruction, visited) = new_program[line]
        if instruction[:3] == 'jmp':
            new_program[line] = (instruction.replace('jmp', 'nop'), visited)
        elif instruction[:3] == 'nop':
            new_program[line] = (instruction.replace('nop', 'jmp'), visited)
        else:
            continue

        accumulator, ran_to_completion = run_program(new_program)
        if ran_to_completion:
            return accumulator

def run_program(program):
    accumulator = 0
    pos = 0
    while True:
        if pos == len(program):
            return (accumulator, True)
        
        (instruction, visited) = program[pos]
        if visited:
            return (accumulator, False)
        else:
            program[pos] = (instruction, True)

        (operation, arg) = instruction.split()
        
        if operation == 'acc':
            accumulator += int(arg)
            pos += 1
        elif operation == 'jmp':
            pos += int(arg)
        else:
            pos += 1

if __name__ == "__main__":
    with open('day8-data.txt') as f:
        input = f.read().splitlines()

        print(part1(input))
        print(part2(input))