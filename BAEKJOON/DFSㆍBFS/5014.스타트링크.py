from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        now, count = queue.popleft()

        if now == g:
            return count

        for nx in (now + u, now - d):
            if 1 <= nx <= f:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append((nx, count + 1))

    return "use the stairs"


f, s, g, u, d = map(int, input().split())
data = [i for i in range(1, f + 1)]
visited = [False] * (f + 1)

print(bfs(s))