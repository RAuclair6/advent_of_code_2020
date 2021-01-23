def part1(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()

    dir = 0
    # dir 0 = East
    # dir 90 = North
    # dir 180 = West
    # dir 270 = South
    # R90 90


    x = 0
    y = 0

    for line in lines:
        print(line, dir)

        if line[0] == 'L':
            dir = (dir + int(line[1:])) % 360
        elif line[0] == 'R':
            dir = (dir - int(line[1:])) % 360

        elif line[0] == 'F':
            if dir == 0:
                x += int(line[1:])
            elif dir == 90:
                y += int(line[1:])
            elif dir == 180:
                x -= int(line[1:])
            elif dir == 270:
                y -= int(line[1:])

        elif line[0] == 'N':
            y += int(line[1:])
        elif line[0] == 'S':
            y -= int(line[1:])
        elif line[0] == 'E':
            x += int(line[1:])
        elif line[0] == 'W':
            x -= int(line[1:])
    
    print(abs(x) + abs(y))




if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day12/aocday12.txt')