s = list(input())
arr1, arr2 = [], []

for c in s:
    if 65 <= ord(c) <= 90:
        arr1.append(c)
    else:
        arr2.append(int(c))

arr1.sort()
print(''.join(arr1) + str(sum(arr2)))