def move():
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                direction = directions[data[i][j] - 1]
                found = False

                for idx in priorities[data[i][j] - 1][direction - 1]:
                    nx = i + dx[idx - 1]
                    ny = j + dy[idx - 1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if remain[nx][ny][1] == 0:
                            directions[data[i][j] - 1] = idx

                            if temp[nx][ny] == 0:
                                temp[nx][ny] = data[i][j]
                            else:
                                temp[nx][ny] = min(data[i][j], temp[nx][ny])
                            found = True
                            break

                if found:
                    continue

                for idx in priorities[data[i][j] - 1][direction - 1]:
                    nx = i + dx[idx - 1]
                    ny = j + dy[idx - 1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if remain[nx][ny][0] == data[i][j]:
                            directions[data[i][j] - 1] = idx
                            temp[nx][ny] = data[i][j]
                            break


    return temp


def update():
    for i in range(n):
        for j in range(n):
            if remain[i][j][1] > 0:
                remain[i][j][1] -= 1

            if data[i][j] != 0:
                remain[i][j] = [data[i][j], k]

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int, input().split()))

priorities = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

remain = [[[0, 0]] * n for _ in range(n)]
answer = 0

while True:
    update()
    new_data = move()
    data = new_data
    answer += 1

    check = True

    for i in range(n):
        for j in range(n):
            if data[i][j] > 1:
                check = False
                break

    if check:
        print(answer)
        break

    if answer >= 1000:
        print(-1)
        break


