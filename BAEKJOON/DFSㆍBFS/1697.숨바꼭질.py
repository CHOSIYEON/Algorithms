from collections import deque

n, k = map(int, input().split())
queue = deque()
queue.append(n)
dist = [0] * 100001

while queue:
    now = queue.popleft()

    if now == k:
        print(dist[now])
        break

    for nx in (now + 1, now - 1, now * 2):
        if 0 <= nx < 100001 and not dist[nx]:
            dist[nx] = dist[now] + 1
            queue.append(nx)

