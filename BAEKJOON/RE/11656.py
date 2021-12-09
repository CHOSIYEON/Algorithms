n = input()
tmp = []

for i in range(len(n)):
    tmp.append(n[i:])

tmp.sort()

for i in tmp:
    print(i)