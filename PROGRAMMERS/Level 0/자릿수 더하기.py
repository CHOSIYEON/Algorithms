def solution(n):
    answer = 0
    for number in str(n):
        answer += int(number)
    return answer

def solution(n):
    return sum(list(map(int,list(str(n)))))