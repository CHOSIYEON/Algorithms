n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
cnt = 0

arr.sort(reverse=True)

first = arr[0]
second = arr[1]

# for i in range(m):
#     if cnt < k:
#         cnt += 1
#         ans += first
#     else:
#         cnt = 0
#         ans += second

ans += first * (m // (k+1)) * k
ans += first * (m % (k+1))
ans += second * (m//(k+1))

print(ans)