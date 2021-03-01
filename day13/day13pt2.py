import math
import itertools

# I got stuck for a long time on this one, then took a break from Advent.
# Can't take credit for the idea behind the solution, which I got from https://www.reddit.com/r/adventofcode/comments/kcb3bb/2020_day_13_part_2_can_anyone_tell_my_why_this/
# But I did implement it myself! 

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
    
    trains = [int(x) for x in trains if x != 'x']

    def trains_time(train_pair, offsets, start_t=0, start_lcm = 1):
        for t in itertools.count(start_t, start_lcm):
            if (t + offsets[0]) % train_pair[0] == 0  and (t + offsets[1]) % train_pair[1] == 0:
                return t, math.lcm(start_lcm, train_pair[0], train_pair[1]) 

    # I think using pairs is actually pointless, but it's what made sense to me when I was working through this, and I get the right answer.

    combs = list(zip([trains[x:x+2] for x in range(0,len(trains))], [diffs[x:x+2] for x in range(0,len(diffs) - 1)]))

    i = 0
    while i < len(combs):
        if i == 0:
            next_start, next_lcm = trains_time(combs[i][0], combs[i][1])
        else:
            next_start, next_lcm = trains_time(combs[i][0], combs[i][1], next_start, next_lcm)
        print(next_start)
        i += 1


if __name__ == '__main__':
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day13/aocday13.txt')
    # part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day13/day13test.txt')
    # part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day13/day13test2.txt')
    # part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day13/day13test3.txt')
    # part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day13/day13test4.txt')
    # part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day13/day13test5.txt')
