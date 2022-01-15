n = int(input())

prime_tmp = [True] * (n+1)
prime_list = []

for i in range(2, n+1):
    if prime_tmp[i]:
        prime_list.append(i)
        for j in range(i*2, n+1, i):
            prime_tmp[j] = False

ans = 0
start, end = 0, 0

while end <= len(prime_list):
    sum_tmp = sum(prime_list[start:end])
    if sum_tmp == n:
        ans += 1
        end += 1
    elif sum_tmp < n:
        end += 1
    else:
        start += 1

print(ans)
