def solution(dirs):
    answer = 0
    visited = []
    x, y = 5, 5
    move = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

    for dir in dirs:
        nx, ny = x + move[dir][0], y + move[dir][1]

        if 0 <= nx < 11 and 0 <= ny < 11:
            if not ([[x, y], [nx, ny]] in visited or [[nx, ny], [x, y]] in visited):
                answer += 1
                visited.append([[x, y], [nx, ny]])

            x, y = nx, ny

    return answer