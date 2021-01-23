# start by counting all the trees you would encounter for the slope right 3, down 1
#  '#' == tree
import numpy

def part1(filepath):

    with open(filepath) as f:
        trees = f.read().splitlines()
    step = 0
    tree_count = 0
    while step < len(trees):
        # print(trees[step][(step*3)%len(trees[step])])
        if step*3 >= len(trees[step]):
            if trees[step][(step*3)%len(trees[step])] == '#':
                tree_count += 1
        elif trees[step][step*3] == '#':
            tree_count += 1
        step += 1
    print(tree_count)


step_pairs = [[1,1], [1,3], [1,5], [1,7], [2,1]]


def part2(filepath, step_pairs):
    tree_counts = []
    with open(filepath) as f:
        trees = f.read().splitlines()
    for pair in step_pairs:
        xstep = 0
        ystep = 0
        tree_count = 0
        while ystep < len(trees):
            if xstep*pair[1] >= len(trees[xstep]):
                if trees[ystep][(xstep*pair[1])%len(trees[xstep])] == '#':
                    tree_count += 1
            elif trees[ystep][xstep*pair[1]] == '#':
                tree_count += 1
            xstep += 1
            ystep += 1*pair[0]
        tree_counts.append(tree_count)
    print(numpy.prod(tree_counts))

if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day3/aocday3.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day3/aocday3.txt', step_pairs)
