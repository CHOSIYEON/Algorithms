s = input()
data = []

for i in range(len(s)):
    data.append(s[i:])

data.sort()

for d in data:
    print(d)