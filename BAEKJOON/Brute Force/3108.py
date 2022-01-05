from collections import deque

def bfs():
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        now = queue.popleft()

        if now == g:
            print(visited[now] - 1)
            return
        else:
            if now + u <= f and visited[now+u] == 0:
                visited[now+u] = visited[now] + 1
                queue.append(now+u)
            if now - d >= 1 and visited[now-d] == 0:
                visited[now-d] = visited[now] + 1
                queue.append(now-d)

    print("use the stairs")


f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)
bfs()