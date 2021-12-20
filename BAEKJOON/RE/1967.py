import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    node, dist = 0, 0
    queue = deque()
    queue.append([num, 0])
    check[num] = True

    while queue:
        new_node, new_dist = queue.popleft()
        for i in tree[new_node]:
            if check[i[0]] == False:
                check[i[0]] = True
                queue.append([i[0], i[1] + new_dist])

                if i[1] + new_dist > dist:
                    dist = i[1] + new_dist
                    node = i[0]

    return node, dist



n = int(input())
tree = [[] * (n+1) for _ in range(n+1)]
check = [False] * (n+1)

for i in range(n-1):
    node1, node2, dist = map(int, input().split())
    tree[node1].append([node2, dist])
    tree[node2].append([node1, dist])

a, b = bfs(1)
check = [False] * (n+1)
print(bfs(a)[1])




