from collections import deque

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j <= Max and not dist[j]: # dist[j] == 0
                dist[j] = dist[x] + 1
                queue.append(j)


n, k = map(int, input().split())
Max = 100000
dist = [0] * (Max+1)

bfs()




