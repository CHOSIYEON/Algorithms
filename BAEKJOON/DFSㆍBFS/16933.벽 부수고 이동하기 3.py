import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    answer = 1
    day = True

    while queue:
        for _ in range(len(queue)):
            x, y, wall = queue.popleft()

            if x == n - 1 and y == m - 1:
                return answer

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 > nx or nx >= n or 0 > ny or ny >= m:
                    continue

                if visited[nx][ny] <= wall:
                    continue

                if data[nx][ny] == 0:
                    queue.append((nx, ny, wall))
                    visited[nx][ny] = wall

                elif wall < k:
                    if not day:
                        queue.append((x, y, wall))
                    else:
                        visited[nx][ny] = wall
                        queue.append((nx, ny, wall + 1))

        answer += 1
        day = not day

    return -1


n, m, k = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[k + 1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())
