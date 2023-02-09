def solution(x):
    answer = False
    arr = []

    for i in str(x):
        arr.append(i)

    arr = list(map(int, arr))

    if x % sum(arr) == 0:
        answer = True

    return answer

