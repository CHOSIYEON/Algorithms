# n, m = map(int, input().split())
# balls = list(map(int, input().split()))
# ans = 0
#
# for i in range(n):
#     for j in range(i+1, n):
#         if balls[i] != balls[j]:
#             ans += 1
#
# print(ans)

n, m = map(int, input().split())
balls = list(map(int, input().split()))
ball_cnt = [0] * 11
ans = 0

for ball in balls:
    ball_cnt[ball] += 1

for i in range(1, m+1):
    n -= ball_cnt[i]
    ans += n * ball_cnt[i]

print(ans)