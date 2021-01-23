import math

# work in progress!

def part2(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    trains = [x for x in lines[1].split(',')]
    
    diffs = []
    diff = 0
    for i in trains:
        if i != 'x':
            diffs.append(diff)
        diff += 1 
    
    print(diffs)  
    trains = [int(x) for x in trains if x != 'x']
    # trains = [int(x) + int(y) for x, y in zip(trains, diffs)]
    print(trains)

    # i = 1
    # while True:
    #     if 



    z = 1
    while z < 1000:
        if (trains[1] * z) % trains[0] == 1:
            print(z, trains[1]*z)
        z += 1
        


if __name__ == '__main__':
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day13/aocday13.txt')

