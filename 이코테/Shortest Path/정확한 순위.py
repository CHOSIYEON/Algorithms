n, m = map(int, input().split())
students = [[1e9] * (n+1) for _ in range(n+1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    students[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            students[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            students[i][j] = min(students[i][j], students[i][k] + students[k][j])

for i in range(1, n+1):
    count = 0

    for j in range(1, n+1):
        if students[i][j] != 1e9 or students[j][i] != 1e9:
            count += 1

    if count == n:
        answer += 1

print(answer)

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4