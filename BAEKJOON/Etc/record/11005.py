n, b = map(int, input().split())
arr = []

while n > 0:
    num = n % b
    if num >= 10:
        arr.append(chr(num + 55))
    else:
        arr.append(str(num))
    n = n // b

arr = reversed(arr)
print(''.join(arr))

