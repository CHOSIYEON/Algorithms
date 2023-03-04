n, m = map(int, input().split())
temp = list(map(int, input().split()))
balls = {i: 0 for i in range(1, m+1)}
answer = 0

for t in temp:
    balls[t] += 1

for i in range(1, m+1):
    a, b = balls[i], 0
    for j in range(i+1, m+1):
        b += balls[j]
    answer += (a * b)

print(answer)
