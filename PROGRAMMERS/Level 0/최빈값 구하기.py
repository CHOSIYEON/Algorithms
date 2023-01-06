def solution(array):
    new_array = []
    for i in set(array):
        new_array.append([i, array.count(i)])

    if len(new_array) == 1:
        return array[0]

    new_array.sort(key=lambda x: x[1], reverse=True)

    return new_array[0][0] if new_array[0][1] != new_array[1][1] else -1