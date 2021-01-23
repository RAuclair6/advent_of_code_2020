def part1(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        lines = [int(x) for x in lines]
        lines.append(0) # charging outlet
        lines.append(max(lines)+3) # tablet
        lines.sort()
    
    pos = 1
    one_diff = 0
    three_diff = 0
    while pos < len(lines):
        if lines[pos] - lines[pos-1] == 1:
            one_diff += 1
        if lines[pos] - lines[pos-1] == 3:
            three_diff += 1
        pos += 1
    print(one_diff * three_diff)
        


# I had to find some hints for this one. I tried recursion at first but there were too many arrangements to brute force.
# A nice introduction to memoisation :)
def part2(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        lines = [int(x) for x in lines]
        lines.append(0) # charging outlet
        lines.append(max(lines)+3) # tablet
        lines.sort()


    cache = {}
    cache[0] = 1

    for i in lines[1:]:
        cache[i] = cache.get(i-1, 0) + cache.get(i-2, 0) + cache.get(i-3, 0)
    
    print(f"{cache[max(cache.keys())]}")


if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day10/aocday10.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day10/aocday10.txt')