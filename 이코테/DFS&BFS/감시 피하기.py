import sys
input = sys.stdin.readline
from collections import deque

def check(data):
    queue = deque()

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'T':
                queue.append((i, j, 0))
                queue.append((i, j, 1))
                queue.append((i, j, 2))
                queue.append((i, j, 3))


    while queue:
        x, y, direction = queue.popleft()

        nx = x + d[direction][0]
        ny = y + d[direction][1]

        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == 'S':
                return False
            elif data[nx][ny] == 'X':
                queue.append((nx, ny, direction))
    return True


def make_walls(count):
    global answer
    if count == 3:
        if check(data):
            answer = 'YES'
        return

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                count += 1
                make_walls(count)
                count -= 1
                data[i][j] = 'X'


n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 우 좌 하
answer = 'NO'

make_walls(0)
print(answer)