import numpy as np

def part2(filepath):
    arr_lists = []
    with open(filepath) as f:
        lines = f.read().splitlines()
    for i in lines:
        arr_lists.append(list(i))
    arr = np.array(arr_lists)
    n = 0
    num_rows, num_cols = arr.shape
    arr_copy = arr.copy()

    def seat_scan(grid, starty, startx):
        neighbors = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
        for dir in directions:
            y_factor = dir[0]
            x_factor = dir[1]

            while True:
                if starty + y_factor >= num_rows:
                    break
                if startx + x_factor >= num_cols:
                    break
                try:
                    if grid[starty+y_factor, startx+x_factor] == 'L' and starty+y_factor>=0 and startx+x_factor>=0:
                        break
                    if grid[starty+y_factor, startx+x_factor] == '#' and starty+y_factor>=0 and startx+x_factor>=0:
                        neighbors += 1
                        break
                except IndexError:
                    break
                x_factor += dir[1]
                y_factor += dir[0]
        return neighbors

    
    while True:

        for x in range(num_cols):
            # print(x)
            for y in range(num_rows):
                # print(y)
                if arr[y,x] == 'L':
                    neighbors = seat_scan(arr,y, x)
                    if neighbors == 0:
                        arr_copy[y,x] = '#'

                elif arr[y,x] == '#':
                    neighbors = seat_scan(arr,y, x)
                    if neighbors >= 5: 
                        arr_copy[y,x] = 'L'
                


        if np.array_equal(arr, arr_copy):
            print(np.count_nonzero(arr == '#'))
            break 
        arr = arr_copy.copy()
        n += 1 


if __name__ == '__main__':
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day11/aocday11.txt')