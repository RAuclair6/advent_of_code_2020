import math

def part1(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    earliest_depart = int(lines[0])
    trains = [int(x) for x in lines[1].replace('x,','').split(',')]

    first_train = None
    

    for train in trains:
        if not first_train:
            first_train = train
        if first_train:
            if -(earliest_depart // -train)*train - earliest_depart < -(earliest_depart // (-1*first_train))*first_train - earliest_depart:
                first_train = train
    # pylint: disable=invalid-unary-operand-type
    print((-(earliest_depart // -first_train)*first_train - earliest_depart) * first_train)

    

if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day13/aocday13.txt')