'''The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). 
Each letter tells you which half of a region the given seat is in.
Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127).
 The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). 
The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

seat ID: multiply the row by 8, then add the column
What is the highest seat ID on a boarding pass?'''

import numpy as np

def part1(filepath):
    with open(filepath) as f:
        partitions = f.read().splitlines()
    
    seat_ids = []

    for partition in partitions:
        rows = [0,128]
        cols = [0,8]
    #rownum
        for dir in partition[:6]:
            if dir == 'F':
                rows[1] = rows[0] + (rows[1] - rows[0])/2
            if dir == 'B':
                rows[0] = rows[1] - (rows[1] - rows[0])/2
        rows[1] = rows[1] - 1
        if partition[6] == 'F':
            row = rows[0]
        if partition[6] == 'B':
            row = rows[1]

        # colnum
        for dir in partition[7:]:
            if dir == 'L':
                cols[1] = cols[0] + (cols[1] - cols[0])/2
            if dir == 'R':
                cols[0] = cols[1] - (cols[1] - cols[0])/2
        cols[1] = cols[1] - 1
        if partition[9] == 'L':
            col = cols[0]
        if partition[9] == 'R':
            col = cols[1]

        
        seat_ids.append(row*8 + col)

    my_seat = list(np.diff(sorted(seat_ids))).index(2)
    print(max(seat_ids), sorted(seat_ids)[my_seat]+1)


if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day5/aocday5.txt')
