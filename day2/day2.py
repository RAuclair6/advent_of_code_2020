# The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# How many passwords are valid?

# 6-7 z: dqzzzjbzz
# split() -> ['6-7', 'z:', 'dqzzzjbzz']

def part1(filepath):
    with open(filepath) as f:
        passwords = f.read().splitlines()
    valid_pws = 0
    for line in passwords:
        letter = line.split()[1][0]
        min_letter = int(line.split()[0].split('-')[0])
        max_letter = int(line.split()[0].split('-')[1])
        pw = line.split()[2]
        if min_letter <= pw.count(letter) <= max_letter: 
            valid_pws += 1
    print(valid_pws)


# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character,
# and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

def part2(filepath):
    with open(filepath) as f:
        passwords = f.read().splitlines()
    valid_pws = 0
    for line in passwords:
        letter = line.split()[1][0]
        first_pos = int(line.split()[0].split('-')[0]) - 1
        second_pos = int(line.split()[0].split('-')[1]) - 1
        pw = line.split()[2]
        if pw[first_pos] == letter and pw[second_pos] == letter:
            continue
        elif pw[first_pos] == letter:
            valid_pws += 1
        elif pw[second_pos] == letter:
            valid_pws += 1
    print(valid_pws)

if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day2/aocday2.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day2/aocday2.txt')