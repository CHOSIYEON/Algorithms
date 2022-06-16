def solution(N):
    answer, cnt = 0, 0
    N = bin(N)[2:]

    for num in N:
        if num == '0':
            cnt += 1
        else:
            answer = max(answer, cnt)
            cnt = 0

    return answer