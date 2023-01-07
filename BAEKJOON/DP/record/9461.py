n = int(input())

def sol(num):
    arr = [1, 1, 1, 2, 2] + [0 for _ in range(num - 5)]
    for i in range(5, num):
        arr[i] = arr[i - 1] + arr[i - 5]
    return arr[num-1]

for i in range(n):
    n = int(input())
    print(sol(n))