def solution(n, arr1, arr2):
    answer = [''] * n
    add = [[0 for _ in range(n)] for _ in range(n)]
    temp1 = [[0 for _ in range(n)] for _ in range(n)]
    temp2 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(arr1)):
        check = []
        while arr1[i] >= 1:
            check.append(arr1[i] % 2)
            arr1[i] //= 2
        temp1[i][:len(check)] = check

    for i in range(len(arr2)):
        check = []
        while arr2[i] >= 1:
            check.append(arr2[i] % 2)
            arr2[i] //= 2
        temp2[i][:len(check)] = check

    for i in range(n):
        for j in range(n - 1, -1, -1):
            add[i][j] = temp1[i][j] + temp2[i][j]
            if add[i][j] != 0:
                answer[i] += '#'
            else:
                answer[i] += ' '

    return answer