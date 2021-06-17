def solution(board, moves):
    answer = 0
    basket = []
    board = list(map(list, zip(*board)))
    for i in moves:
        for j in range(len(board[0])):
            if board[i-1][j] != 0:
                basket.append(board[i-1][j])
                board[i-1][j] = 0
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        answer += 2
                break
    return answer