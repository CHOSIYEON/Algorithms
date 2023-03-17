import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

visited[r][c] = True
answer = 1

while True:
    for _ in range(4):
        d = (d + 3) % 4
        nx = r + directions[d][0]
        ny = c + directions[d][1]

        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            continue

        if data[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            answer += 1
            r, c = nx, ny
            break
    else:
        if data[r - directions[d][0]][c - directions[d][1]] == 1:
            print(answer)
            break
        else:
            r -= directions[d][0]
            c -= directions[d][1]

