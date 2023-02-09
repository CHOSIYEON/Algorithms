def solution(n):
    answer = n + 1

    while True:
        if bin(answer)[2:].count('1') == bin(n)[2:].count('1'):
            return answer
        answer += 1