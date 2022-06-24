# 시간 초과
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        price = prices.popleft()
        time = 0

        for i in range(len(prices)):
            time += 1
            if price > prices[i]:
                break

        answer.append(time)

    return answer


# 통과
def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        now = prices[i]
        cnt = 0

        for j in range(i + 1, len(prices)):
            cnt += 1
            if now > prices[j]:
                break
        answer.append(cnt)

    return answer + [0]