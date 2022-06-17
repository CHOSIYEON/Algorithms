import sys
from collections import deque
input = sys.stdin.readline

r, c, n = map(int, input().split())
data = [list(input().rstrip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

def bfs(queue, data):
    while queue:
        x, y = queue.popleft()
        data[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and data[nx][ny] == 'O':
                data[nx][ny] = '.'

def simulate(time):
    global data, queue
    if time == 1:
        for i in range(r):
            for j in range(c):
                if data[i][j] == 'O': # 처음 터지는 폭탄 먼저 넣기
                    queue.append((i, j))
    elif time % 2 == 1: # 폭탄 터짐
        bfs(queue, data)
        for i in range(r):
            for j in range(c):
                if data[i][j] == 'O':
                    queue.append((i, j)) # 다음에 터질 폭탄 넣기
    else:
        data = [['O'] * c for _ in range(r)]

for i in range(1, n+1):
    simulate(i)

for row in data:
    print(''.join(row))

##

import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

def install(time):
    for i in range(r):
        for j in range(c):
            if not graph[i][j]:
                graph[i][j] += (time+3)

def check(time):
    queue = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == time:
                queue.append((i, j))

    bomb(queue)

def bomb(queue):
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                graph[nx][ny] = 0


r, c, n = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(r):
    temp = list(input().rstrip())

    for i in range(len(temp)):
        if temp[i] == '.':
            temp[i] = 0
        else:
            temp[i] = 3

    graph.append(temp)

for time in range(2, n+1):
    install(time)
    check(time)

for i in graph:
    for j in i:
        if not j:
            print('.', end='')
        else:
            print('O',end='')
    print()
