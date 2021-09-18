# import sys
# input = sys.stdin.readline
#
# n = int(input())
# matrix = []
# result = [0, 0, 0]
#
# def check(start_x, start_y, n):
#     temp = matrix[start_x][start_y]
#     for i in range(n):
#         for j in range(n):
#             if temp != matrix[start_x + i][start_y + j]:
#                 return False
#     return True
#
# def divide(start_x, start_y, n):
#     if check(start_x, start_y, n):
#         result[matrix[start_x][start_y]+1] += 1
#     else:
#         for i in range(3):
#             for j in range(3):
#                 divide(start_x + i * n//3, start_y + j * n//3, n//3)
#
#     return 0
#
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# divide(0, 0, n)
#
# for i in result:
#     print(i)

import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
count_0, count_1, count_m1 = 0, 0, 0

def divide(x, y, n):
    global count_0, count_1, count_m1
    check = matrix[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != matrix[i][j]:
                check = -2
                break

    if check == -2:
        n = n//3
        for i in range(3):
            for j in range(3):
                divide(x + i*n, y + j*n, n)
    elif check == 0:
        count_0 += 1
    elif check == 1:
        count_1 += 1
    elif check == -1:
        count_m1 += 1

divide(0, 0, n)
print(count_m1)
print(count_0)
print(count_1)

