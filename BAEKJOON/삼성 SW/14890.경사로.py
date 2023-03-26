import sys
input = sys.stdin.readline

def check(array):
    for i in range(1, n):
        if abs(array[i] - array[i - 1]) > 1:
            return False

        if array[i] < array[i - 1]:
            for j in range(l):
                if i + j >= n or array[i] != array[i + j] or slope[i + j]:
                    return False
                if array[i] == array[i + j]:
                    slope[i + j] = True
        elif array[i] > array[i - 1]:
            for j in range(l):
                if i - j - 1 < 0 or array[i - 1] != array[i - j - 1] or slope[i - j - 1]:
                    return False
                if array[i - 1] == array[i - j - 1]:
                    slope[i - j - 1] = True

    return True


n, l = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    slope = [False] * n
    if check([data[i][j] for j in range(n)]):
        answer += 1

for j in range(n):
    slope = [False] * n
    if check([data[i][j] for i in range(n)]):
        answer += 1

print(answer)
