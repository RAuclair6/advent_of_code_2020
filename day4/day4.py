import re


# The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields.
#  The expected fields are as follows:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)


def part1(filepath):

    needed_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    id_count = 0

    with open(filepath) as f:
        ids = f.read().split('\n\n')
    for id in ids:
        if all(field in id for field in needed_fields):
            id_count += 1
    print(id_count)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def part2(filepath):

    id_count = 0


    def birth_check(field, checks):
        if len(field) == 4 and 1920 <= int(field) <= 2002:
            checks.append(1)

    def issue_check(field, checks):
        if len(field) == 4 and 2010 <= int(field) <= 2020:
            checks.append(1)

    def exp_check(field, checks):
        if len(field) == 4 and 2020 <= int(field) <= 2030:
            checks.append(1)

    def height_check(field, checks):
        height = list(filter(None, re.split(r'(\d+)', field)))
        if len(height) == 2:
            if height[1] == 'cm':
                if 150 <= int(height[0]) <= 193:
                    checks.append(1)
            elif height[1] == 'in':
                if 59 <= int(height[0]) <= 76:
                    checks.append(1)

    def hair_check(field, checks):
        if re.search(r'#[\da-f]{6}', field):
            checks.append(1)

    def eye_check(field, checks):
        valid_eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if field in valid_eyes:
            checks.append(1)

    def pass_check(field, checks):
        if re.search(r'^[\d]{9}$', field):
            checks.append(1)

    with open(filepath) as f:
        ids = f.read().split('\n\n')
    for id in ids:
        fieldchecks = []
        for field in re.split(' |\n', id):
            if field.split(':')[0] == 'byr':
                birth_check(field.split(':')[1], fieldchecks)        
            if field.split(':')[0] == 'iyr':
                issue_check(field.split(':')[1], fieldchecks)
            if field.split(':')[0] == 'eyr':
                exp_check(field.split(':')[1], fieldchecks)
            if field.split(':')[0] == 'hgt':
                height_check(field.split(':')[1], fieldchecks)
            if field.split(':')[0] == 'hcl':
                hair_check(field.split(':')[1], fieldchecks)
            if field.split(':')[0] == 'ecl':
                eye_check(field.split(':')[1], fieldchecks)
            if field.split(':')[0] == 'pid':
                pass_check(field.split(':')[1], fieldchecks)
        if len(fieldchecks) == 7:
            id_count += 1
    print(id_count)

if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day4/aocday4.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day4/aocday4.txt')