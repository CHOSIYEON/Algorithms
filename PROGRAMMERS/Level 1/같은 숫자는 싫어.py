def solution(arr):
    answer = []
    answers = [0] * len(arr)

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            answers[i + 1] = 1

    for i in range(len(arr)):
        if answers[i] == 0:
            answer.append(arr[i])

    return answer