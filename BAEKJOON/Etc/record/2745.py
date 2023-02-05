n, b = map(str, input().split())
n = list(reversed(list(n)))
b = int(b)
sum = 0

for i in range(len(n)):
    if n[i].isalpha():
        n[i] = int(ord(n[i])-55)
    sum = sum + pow(b, i) * int(n[i])

print(sum)