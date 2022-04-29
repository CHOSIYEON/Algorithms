from collections import deque

def solution(boards, moves):
    answer = 0
    basket = []
    board = [deque() for _ in range(len(boards))]

    for temp in boards:
        for i in range(len(boards)):
            if temp[i] != 0:
                board[i].append(temp[i])

    for move in moves:
        if len(board[move - 1]) == 0:
            continue

        basket.append(board[move - 1].popleft())

        if len(basket) >= 2:
            a = basket[-1]
            b = basket[-2]

            if a == b:
                answer += 2
                basket = basket[:-2]

    return answer