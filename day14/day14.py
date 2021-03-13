import re
import itertools

def part1(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    
    memstore = {}
    for line in lines:
        if line[:4] == 'mask':
            # get the stuff after = and save that as bitmask to use for subsequent mem inputs
            mask = line[7:]
        else:
            # convert the stuff after = to binary, apply bitmask, save that to a dict with [mem address] = value
            val = bin(int(re.search(r'= (.*)',line)[1]))[2:].zfill(36)
            masked = []
            for i in range(len(val)):
                if mask[i] != 'X':
                    masked.append(mask[i])
                else:
                    masked.append(val[i])
            memstore[re.search(r'mem\[(.*)\]',line)[1]] = ''.join(masked)
    
    print(sum([int(x,2) for x in list(memstore.values())]))

def part2(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    
    memstore = {}
    for line in lines:
        if line[:4] == 'mask':
            mask = line[7:]
        else:
            val = int(re.search(r'= (.*)',line)[1])
            add = bin(int(re.search(r'mem\[(.*)\]',line)[1]))[2:].zfill(36)
            masked = []
            for i in range(len(add)):
                if mask[i] == '0':
                    masked.append(add[i])
                elif mask[i] == '1':
                    masked.append('1')
                elif mask[i] == 'X':
                    masked.append('X')
            add = ''.join(masked)
            for j in [''.join(map(str, x)) for x in itertools.product([0,1], repeat=add.count('X'))]:
                j = list(j)
                temp = []
                for z in add:
                    if z != 'X':
                        temp.append(z)
                    else:
                        temp.append(j.pop(0))
                memstore[''.join(temp)] = val 

    print(sum([int(x) for x in list(memstore.values())]))


if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day14/aocday14.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day14/aocday14.txt')
