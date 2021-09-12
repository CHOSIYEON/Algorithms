import sys
input = sys.stdin.readline

n = int(input())
matrix = []
result = [0, 0, 0]

def check(start_x, start_y, n):
    temp = matrix[start_x][start_y]
    for i in range(n):
        for j in range(n):
            if temp != matrix[start_x + i][start_y + j]:
                return False
    return True

def divide(start_x, start_y, n):
    if check(start_x, start_y, n):
        result[matrix[start_x][start_y]+1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(start_x + i * n//3, start_y + j * n//3, n//3)

    return 0

for i in range(n):
    matrix.append(list(map(int, input().split())))

divide(0, 0, n)

for i in result:
    print(i)


