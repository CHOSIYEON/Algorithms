n, m = map(int, input().split())
balls = list(map(int, input().split()))
balls_w = [0] * (m+1)
ans = 0

for i in balls:
    balls_w[i] += 1

for i in range(1, m+1):
    n -= balls_w[i]
    ans += balls_w[i] * n

print(ans)

# for i in range(1, m+1):
#     ans += (balls_w[i] * sum(balls_w[i+1:]))
