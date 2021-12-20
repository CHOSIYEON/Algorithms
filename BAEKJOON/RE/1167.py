import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    dist, node = 0, 0
    queue = deque()
    queue.append([num, 0])
    check[num] = True
    while queue:
        now, now_dist = queue.popleft()
        for i in graph[now]:
            if check[i[0]] == False:
                check[i[0]] = True
                queue.append((i[0], i[1] + now_dist))

                if now_dist + i[1] > dist:
                    dist = now_dist + i[1]
                    node = i[0]
    return dist, node

n = int(input())
graph = [[] * n for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(1, len(line)-1, 2):
        graph[line[0]-1].append([line[j]-1, line[j+1]])

check = [False] * n
a, b = bfs(0)

check = [False] * n
print(bfs(b)[0])

