def part1(filepath):
    all_answers = []
    with open(filepath) as f:
        forms = f.read().split('\n\n')
    for form in forms:
        group_answers = []
        for answer in form.replace('\n', ''):
            if answer not in group_answers:
                group_answers.append(answer)
        all_answers.append(group_answers)
    tot_answers = 0
    for group_answer in all_answers:
        tot_answers += len(group_answer)

    print(tot_answers)


def part2(filepath):
    all_answers = []
    with open(filepath) as f:
        forms = f.read().split('\n\n')
    for form in forms:
        group_answers = []
        for split_form in form.split('\n'):
            if not group_answers:
                for answer in split_form:
                    group_answers.append(answer)
            elif group_answers:
                for answer in group_answers.copy(): # tricky... need to make a copy because removing elements causes you to skip the next element in the original list completely
                    if answer not in split_form:
                        group_answers.remove(answer)
            if not group_answers:
                break
        all_answers.append(group_answers)
    tot_answers = 0
    for group_answer in all_answers:
        tot_answers += len(group_answer)

    print(tot_answers)


if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day6/aocday6.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day6/aocday6.txt')