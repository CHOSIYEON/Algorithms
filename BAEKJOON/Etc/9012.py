n = int(input())

for i in range(n):
    arr = list(map(str, input()))
    check = 0
    idx = 0
    while check >= 0:
        if arr[idx] == '(':
            check += 1
        elif arr[idx] == ')':
            check -= 1

        if idx == len(arr)-1:
            break
        else:
            idx += 1

    if check == 0:
        print('YES')
    else:
        print('NO')