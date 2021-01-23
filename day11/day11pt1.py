import numpy as np

def part1(filepath):
    arr_lists = []
    with open(filepath) as f:
        lines = f.read().splitlines()
    for i in lines:
        arr_lists.append(list(i))
    arr = np.array(arr_lists)
    n = 0
    # return arr

    
    while True:
        num_rows, num_cols = arr.shape
        arr_copy = arr.copy()
        for x in range(num_cols):
            for y in range(num_rows):
                if arr[y,x] == 'L':
                    neighbors = 0
                    for i in [x-1, x, x+1]:
                        if not 0 <= i <= num_cols-1:
                            continue
                        for j in [y-1, y, y+1]:
                            if not 0 <= j <= num_rows-1:
                                continue
                            if arr[j,i] == '#':
                                neighbors += 1
                    if neighbors == 0:
                        arr_copy[y,x] = '#'
                elif arr[y,x] == '#':
                    neighbors = 0
                    for i in [x-1, x, x+1]:
                        if not 0 <= i <= num_cols-1:
                            continue
                        for j in [y-1, y, y+1]:
                            if not 0 <= j <= num_rows-1:
                                continue
                            if arr[j,i] == '#':
                                neighbors += 1
                    if neighbors >= 5: #we end up counting the chair itself, so increase 'neighbor' requirement  
                        arr_copy[y,x] = 'L'
        if np.array_equal(arr, arr_copy):
            print(np.count_nonzero(arr == '#'))
            break 
        arr = arr_copy.copy()
        n += 1

if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day11/aocday11.txt')