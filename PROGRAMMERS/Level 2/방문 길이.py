def solution(dirs):
    answer = 0
    prev_x, prev_y = 0, 0
    cmd = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    check = []

    for dir in dirs:
        now_x = prev_x + cmd[dir][0]
        now_y = prev_y + cmd[dir][1]

        if -5 > now_x or now_x > 5 or -5 > now_y or now_y > 5:
            continue

        for c in check:
            if [now_x, now_y] in c and [prev_x, prev_y] in c:
                break
        else:
            answer += 1

        check.append([[now_x, now_y], [prev_x, prev_y]])
        prev_x, prev_y = now_x, now_y

    return answer

######

def solution(dirs):
    x, y = 0, 0
    cmd = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    check = set()

    for dir in dirs:
        nx = x + cmd[dir][0]
        ny = y + cmd[dir][1]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            check.add((x, y, nx, ny))
            check.add((nx, ny, x, y))
            x, y = nx, ny

    return len(check) // 2