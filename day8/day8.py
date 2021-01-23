def part1(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()


    def game_exe(code):
        executed = []
        accumulator = 0
        instruction = 0
        while True:
            if instruction in executed:
                print(accumulator)
                break
            if code[instruction].split(' ')[0] == 'acc':
                accumulator += int(code[instruction].split(' ')[1])
                executed.append(instruction)
                instruction += 1
            if code[instruction].split(' ')[0] == 'nop':
                executed.append(instruction)
                instruction += 1
            if code[instruction].split(' ')[0] == 'jmp':
                executed.append(instruction)
                instruction += int(code[instruction].split(' ')[1])
    
    game_exe(lines)
            

def part2(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()


    def game_exe(code):
        line_num = 0
        while line_num < len(code):
                executed = []
                accumulator = 0
                instruction = 0
                if code[line_num].split(' ')[0] == 'acc':
                    line_num += 1 
                    continue
                # iterate through all instructions, making changes to a single nop or jmp per run
                if code[line_num].split(' ')[0] == 'nop':
                    code[line_num] = code[line_num].replace('nop', 'jmp')
                elif code[line_num].split(' ')[0] == 'jmp':
                    code[line_num] = code[line_num].replace('jmp', 'nop')
                while True:
                    if instruction in executed:
                        #undo the change if it didn't result in code execulting correctly
                        if code[line_num].split(' ')[0] == 'nop':
                            code[line_num] = code[line_num].replace('nop', 'jmp')
                        elif code[line_num].split(' ')[0] == 'jmp':
                            code[line_num] = code[line_num].replace('jmp', 'nop')
                        line_num += 1
                        break
                    if instruction == 617:
                        print(accumulator)
                        return accumulator
                    if code[instruction].split(' ')[0] == 'acc':
                        accumulator += int(code[instruction].split(' ')[1])
                        executed.append(instruction)
                        instruction += 1
                    if code[instruction].split(' ')[0] == 'nop':
                        executed.append(instruction)
                        instruction += 1
                    if code[instruction].split(' ')[0] == 'jmp':
                        executed.append(instruction)
                        instruction += int(code[instruction].split(' ')[1])
        # print(code)

    
    game_exe(lines)


if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day8/aocday8.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day8/aocday8.txt')