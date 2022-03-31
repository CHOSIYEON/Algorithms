# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = []
#
# for i in arr:
#     ans.append(min(i))
#
# print(max(ans))

n, m = map(int, input().split())
ans = -1e9

for _ in range(n):
    temp = list(map(int, input().split()))
    ans = max(min(temp), ans)

print(ans)