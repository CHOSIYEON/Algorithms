def solution(array, height):
    array = sorted(array)

    for idx, value in enumerate(array):
        if value > height:
            return len(array) - idx
    return 0

#######

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)