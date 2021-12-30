import sys
input = sys.stdin.readline

def divide(x, y, n):
    check = trees[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != trees[i][j]:
                check = -1
                break

    if check == -1:
        n = n // 2
        print("(", end='')
        for i in range(2):
            for j in range(2):
                divide(x + i * n, y + j * n, n)
        print(")", end='')
    elif check == 0:
        print("0", end='')
    elif check == 1:
        print("1", end='')



n = int(input())
trees = [list(map(int, input().strip())) for _ in range(n)]

divide(0, 0, n)
