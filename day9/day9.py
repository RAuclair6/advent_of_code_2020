

def part1(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        lines = [int(x) for x in lines]
    i = 25
    while i < len(lines):
        target = lines[i]
        fails = []
        for z in lines[i-25:i]:
            if target - z in lines[i-25:i] and target - z != z:
                i += 1
                break
            fails.append(z)
        if len(fails) == 25:
            print(target)
            return target
        

def part2(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        lines = [int(x) for x in lines]
    target = part1(filepath)
    list_len = 2
    while list_len < len(lines):
        pos = 0
        # print('iterating through lists this long: ' + str(list_len))
        while pos < len(lines):
            # print('start_pos: ' + str(pos))
            if not all(i < target for i in lines[pos:pos+list_len]):
                pos += 1 
                continue
            if sum(lines[pos:pos+list_len]) == target:
                return print(max(lines[pos:pos+list_len]) + min(lines[pos:pos+list_len]))
            pos += 1
        list_len += 1

if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day9/aocday9.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day9/aocday9.txt')