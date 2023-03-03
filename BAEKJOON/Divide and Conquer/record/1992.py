import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().strip())) for _ in range(n)]

def divide(x, y, n):
    global result
    check = matrix[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != matrix[i][j]:
                check = -1
                break

    if check == -1:
        n = n//2
        print("(", end='')
        divide(x, y, n)
        divide(x, y + n, n)
        divide(x + n, y, n)
        divide(x+n, y+n, n)
        print(")", end='')
    elif check == 1:
        print("1", end='')
    elif check == 0:
        print("0", end='')


divide(0, 0, n)
