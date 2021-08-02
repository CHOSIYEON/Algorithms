n = int(input())
answer = [0] * (n+2)
answer[1] = 1

for i in range(2, n+2):
    answer[i] = answer[i-1] + answer[i-2]

print(answer[n+1] % 10007)