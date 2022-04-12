def check(x, y, place):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 대각선
    dx2 = [-1, -1, 1, 1]
    dy2 = [-1, 1, -1, 1]

    # 거리 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] == 'P':
                return False

    # 거리 2 (상하좌우)
    for i in range(4):
        nx = x + 2 * dx[i]
        ny = y + 2 * dy[i]

        nx2 = x + dx[i]
        ny2 = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] == 'P':
                if place[nx2][ny2] != 'X':
                    return False

    # 거리 2 (대각선)
    for i in range(4):
        nx = x + dx2[i]
        ny = y + dy2[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] == 'P':
                if place[nx][y] != 'X' or place[x][ny] != 'X':
                    return False

    return True


def solve(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                flag = check(i, j, place)
                if not flag:
                    return False

    return True


def solution(places):
    answer = []

    for place in places:
        if solve(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer