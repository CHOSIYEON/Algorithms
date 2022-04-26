import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = []
teachers = []
temp = [[0] * n for _ in range(n)]
find = False

for i in range(n):
    data.append(list(map(str, input().split())))
    for j in range(n):
        if data[i][j] == 'T':
            teachers.append((i, j))


def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if temp[x][y] == 'S':
                return True
            elif temp[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if temp[x][y] == 'S':
                return True
            elif temp[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if temp[x][y] == 'S':
                return True
            elif temp[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if temp[x][y] == 'S':
                return True
            elif temp[x][y] == 'O':
                return False
            x += 1


def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


def dfs(count):
    global find

    if count == 3:
        for x in range(n):
            for y in range(n):
                temp[x][y] = data[x][y]

        if not process():
            find = True

        return

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                count += 1
                dfs(count)
                count -= 1
                data[i][j] = 'X'


dfs(0)

if not find:
    print("NO")
else:
    print("YES")