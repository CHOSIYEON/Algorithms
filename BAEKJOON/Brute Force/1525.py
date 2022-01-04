import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(puzzle)
    visited[puzzle] = 1

    while queue:
        puz = queue.popleft()

        if puz == '123456780':
            return visited[puz]

        target = puz.index('0')
        tx = target // 3
        ty = target % 3

        for i in range(4):
            nx = dx[i] + tx
            ny = dy[i] + ty

            if 0 <= nx < 3 and 0 <= ny < 3:
                t = 3 * nx + ny
                tmp = list(puz)
                tmp[target], tmp[t] = tmp[t], tmp[target]
                new_puzzle = ''.join(tmp)

                if not visited.get(new_puzzle):
                    visited[new_puzzle] = visited[puz] + 1
                    queue.append(new_puzzle)

    return -1


puzzle = ''
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = dict()


for i in range(3):
    puzzle += ''.join(list(input().split()))

print(bfs())