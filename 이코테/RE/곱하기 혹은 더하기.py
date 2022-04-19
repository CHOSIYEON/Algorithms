numbers = list(map(int, input()))
ans = numbers[0]

for i in range(1, len(numbers)):
    if ans <= 1 or numbers[i] <= 1:
        ans += numbers[i]
    else:
        ans *= numbers[i]

print(ans)