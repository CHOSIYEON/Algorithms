import sys
input = sys.stdin.readline

def cal(prev, idx):
    global add, sub, mul, div, max_value, min_value

    if idx == n:
        max_value = max(max_value, prev)
        min_value = min(min_value, prev)
        return

    if add > 0:
        add -= 1
        cal(prev + data[idx], idx + 1)
        add += 1
    if sub > 0:
        sub -= 1
        cal(prev - data[idx], idx + 1)
        sub += 1
    if mul > 0:
        mul -= 1
        cal(prev * data[idx], idx + 1)
        mul += 1
    if div > 0:
        div -= 1
        cal(int(prev / data[idx]), idx + 1)
        div += 1


n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value, min_value = -1e9, 1e9

cal(data[0], 1)
print(max_value)
print(min_value)

