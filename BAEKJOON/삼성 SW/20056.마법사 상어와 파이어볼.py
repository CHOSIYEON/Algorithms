from collections import deque

def move():
    while fireballs:
        r, c = fireballs.popleft()
        m, s, d = data[r][c].popleft()

        nr = (r + dx[d] * s) % n
        nc = (c + dy[d] * s) % n

        data[nr][nc].append(deque((m, s, d)))

    for i in range(n):
        for j in range(n):
            if len(data[i][j]) > 1:
                mass, speed = 0, 0
                count = [0, 0]
                length = len(data[i][j])

                while data[i][j]:
                    m, s, d = data[i][j].popleft()
                    mass += m
                    speed += s
                    count[d % 2] += 1

                if mass // 5 == 0:
                    continue

                if count[0] * count[1] == 0:
                    directions = [0, 2, 4, 6]
                else:
                    directions = [1, 3, 5, 7]

                for direction in directions:
                    fireballs.append((i, j))
                    data[i][j].append(deque((mass // 5, speed // length, direction)))
            elif len(data[i][j]) == 1:
                fireballs.append((i, j))


n, m, k = map(int, input().split())
fireballs = deque()
data = [[deque() for _ in range(n)] for _ in range(n)]
answer = 0

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1))
    data[r - 1][c - 1].append((deque((m, s, d))))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    move()

for i in range(n):
    for j in range(n):
        answer += sum(arr[0] for arr in data[i][j])

print(answer)