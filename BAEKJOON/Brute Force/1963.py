import sys
from collections import deque
input = sys.stdin.readline

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def bfs(a, b):
    queue = deque()
    queue.append([a, 0])
    visited = [0] * 10000

    while queue:
        x, cnt = queue.popleft()
        visited[x] = 1
        strX = str(x)

        if x == b:
            return cnt

        for i in range(4):
            for j in range(10):
                tmp = int(strX[:i] + str(j) + strX[i+1:])

                if visited[tmp] == 0 and is_prime_number(tmp) and tmp >= 1000:
                    visited[tmp] = 1
                    queue.append([tmp, cnt + 1])



n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    ans = bfs(a, b)

    if ans != None:
        print(ans)
    else:
        print("Impossible")