n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

count = m // (k+1) * k + m % (k+1)

print(arr[0] * count + arr[1] * (m-count))