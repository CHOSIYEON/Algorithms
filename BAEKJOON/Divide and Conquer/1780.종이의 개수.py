import sys
input = sys.stdin.readline

def count(x, y, n):
    now = papers[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if papers[i][j] != now:
                for k in range(3):
                    for l in range(3):
                        count(x + k * n // 3, y + l * n // 3, n // 3)
                return
    else:
        answer[now] += 1


n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
answer = {-1: 0, 0: 0, 1:0}

count(0, 0, n)

for i in answer.values():
    print(i)
