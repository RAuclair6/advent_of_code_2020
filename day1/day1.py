# pt. 1 find the two entries that sum to 2020 and then multiply those two numbers together

def part1(filepath):
    with open(filepath) as f:
        expense_report = f.read().splitlines() 
    expense_report = [int(item) for item in expense_report]

    x = 0
    while x < len(expense_report) - 2:
        y = x + 1
        while y < len(expense_report) - 1:
            if expense_report[x] + expense_report[y] == 2020:
                print(expense_report[x] * expense_report[y])
            y += 1
        x += 1



# what is the product of the three entries that sum to 2020?

def part2(filepath):
    with open(filepath) as f:
        expense_report = f.read().splitlines() 
    expense_report = [int(item) for item in expense_report]

    x = 0
    while x < len(expense_report) - 3:
        y = x + 1
        while y < len(expense_report) - 2:
            z = y + 1
            while z < len(expense_report) - 1:
                if expense_report[x] + expense_report[y] + expense_report[z] == 2020:
                    print(expense_report[x] * expense_report[y] * expense_report[z])
                z += 1
            y += 1
        x += 1


if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day1/aocday1.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day1/aocday1.txt')
