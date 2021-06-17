from itertools import combinations

def solution(nums):
    answer = 0
    nums = list(combinations(nums, 3))

    for i in range(len(nums)):
        total = sum(nums[i])
        check = True
        for j in range(2, total):
            if total % j == 0:
                check = False
                break
        if check:
            answer += 1
    return answer