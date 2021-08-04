# 계산 잘못해서 점화식을 못찾음

n = int(input())


def sol(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return sol(num - 1) + sol(num - 2) + sol(num - 3)


for i in range(n):
    inp = int(input())
    print(sol(inp))
