n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

arr.sort(reverse=True)
num1 = arr[0]
num2 = arr[1]

if num1 == num2:
    ans = m * num1
else:
    cnt = m//(k+1)
    ans = cnt * (k*num1 + num2) + (m-cnt*(k+1)) * num1

print(ans)

