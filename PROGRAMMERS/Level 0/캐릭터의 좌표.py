def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    max_x, max_y = board[0] // 2, board[1] // 2

    for key in keyinput:
        if key == "left":
            if -max_x <= x - 1 <= max_x:
                x -= 1
        elif key == "right":
            if -max_x <= x + 1 <= max_x:
                x += 1
        elif key == "up":
            if -max_y <= y + 1 <= max_y:
                y += 1
        else:
            if -max_y <= y - 1 <= max_y:
                y -= 1
    return [x, y]