def solution(nums):
    answer = 0
    able = len(set(nums))
    answer = min(able, len(nums)/2)
    return answer