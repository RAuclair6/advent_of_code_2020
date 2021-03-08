puzzle = [13,0,10,12,1,5,8]
# test1 = [0,3,6]
# test2 = [1,3,2]
# test3 = [2,1,3]

def solution(nums, turns):
    called = {b:[a+1] for a,b in enumerate(nums[:-1])}
    next_num = nums[-1]
    for i in range(len(nums)-1, turns-1):
        if next_num in called:
            called[next_num].append(i+1)
            next_num = called[next_num][-1] - called[next_num][-2]    
        else:
            called[next_num] = [i+1]
            next_num = 0
    print(next_num)

# part1(test1)
# part1(test2)
# part1(test3)
solution(puzzle,2020)
solution(puzzle,30000000)
