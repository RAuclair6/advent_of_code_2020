def part2(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()

    # dir 0 = East
    # dir 90 = North
    # dir 180 = West
    # dir 270 = South
    # 106130

    ship_x = 0
    ship_y = 0

    waypoint_x = 10
    waypoint_y = 1

    for line in lines:

        if line[0] == 'L':
            if int(line[1:]) == 90:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            if int(line[1:]) == 180:
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            if int(line[1:]) == 270:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif line[0] == 'R':
            if int(line[1:]) == 90:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
            if int(line[1:]) == 180:
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            if int(line[1:]) == 270:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x

        elif line[0] == 'F':
            ship_x += int(line[1:]) * waypoint_x
            ship_y += int(line[1:]) * waypoint_y

        elif line[0] == 'N':
            waypoint_y += int(line[1:])
        elif line[0] == 'S':
            waypoint_y -= int(line[1:])
        elif line[0] == 'E':
            waypoint_x += int(line[1:])
        elif line[0] == 'W':
            waypoint_x -= int(line[1:])

        
    print(abs(ship_x) + abs(ship_y))


if __name__ == '__main__':
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day12/aocday12.txt')