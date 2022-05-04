from collections import deque


def check(place):
    students = deque()

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                students.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dx2 = [1, 1]
    dy2 = [-1, 1]

    while students:
        x, y = students.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            nx2 = x + dx[i] * 2
            ny2 = y + dy[i] * 2

            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[nx][ny] == 'P':
                    return False

            if 0 <= nx2 < 5 and 0 <= ny2 < 5:
                if place[nx2][ny2] == 'P':
                    if place[nx][ny] != 'X':
                        return False

        for i in range(2):
            nx = x + dx2[i]
            ny = y + dy2[i]

            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[nx][ny] == 'P':
                    if place[nx][y] != 'X' or place[x][ny] != 'X':
                        return False

    return True


def solution(places):
    answer = []

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer