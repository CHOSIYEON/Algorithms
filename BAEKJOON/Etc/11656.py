n = input()
arr = []

for i in range(len(n)):
    arr.append(n[i:])


for i in sorted(arr):
    print(i)