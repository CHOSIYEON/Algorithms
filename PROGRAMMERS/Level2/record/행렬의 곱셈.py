def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            temp2 = 0
            for m in range(len(arr1[0])):
                temp2 += arr1[i][m] * arr2[m][j]
            temp.append(temp2)
        answer.append(temp)

    return answer