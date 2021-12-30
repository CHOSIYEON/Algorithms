import sys
input = sys.stdin.readline

def check(x, y, n):
    global plus_count, zero_count, minus_count
    temp = papers[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if temp != papers[i][j]:
                temp = -2
                break

    if temp == -2:
        n = n//3
        for i in range(3):
            for j in range(3):
                check(x + i * n, y + j * n, n)
    elif temp == 1:
        plus_count += 1
    elif temp == 0:
        zero_count += 1
    elif temp == -1:
        minus_count += 1


n = int(input())
papers = []

minus_count = 0
zero_count = 0
plus_count = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    papers.append(tmp)

check(0, 0, n)
print(minus_count)
print(zero_count)
print(plus_count)

