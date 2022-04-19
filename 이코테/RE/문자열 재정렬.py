arr = list(map(str, input()))
num = 0
s = []

for x in arr:
    if x.isalpha():
        s.append(x)
    else:
        num += int(x)

s.sort()

print(''.join(s),end='')
print(num)