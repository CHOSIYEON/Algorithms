import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def quad_tree(x, y, n):
    now = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != now:
                print("(", end='')
                for k in range(2):
                    for l in range(2):
                        quad_tree(x + k * n // 2, y + l * n // 2, n // 2)
                print(")", end='')
                return
    else:
        print(now, end='')


n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

quad_tree(0, 0, n)