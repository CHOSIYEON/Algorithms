import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input())
directions = []

for _ in range(l):
    directions.append(list(map(str, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction, time = 0, 0
change = 0
x, y = 0, 0
queue = deque()
queue.append((x, y))

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 > nx or nx >= n or 0 > ny or ny >= n or (nx, ny) in queue:
        break

    queue.append((nx, ny))

    if board[nx][ny] == 0:
        queue.popleft()
    else:
        board[nx][ny] = 0

    x, y = nx, ny
    time += 1

    if change < len(directions) and time == int(directions[change][0]):
        if directions[change][1] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        change += 1

print(time + 1)
