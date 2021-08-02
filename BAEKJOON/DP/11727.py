n = int(input())
answer = [0] * (n+1)
answer[0] = 1
answer[1] = 3

for i in range(2,n+1):
    answer[i] = answer[i-1] + answer[i-2] * 2

print(answer[n-1] % 10007)