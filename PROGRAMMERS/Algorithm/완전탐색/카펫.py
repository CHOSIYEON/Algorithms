def checkCarpet(h, w, brown):
    brown_cnt = (h + 2) * (w + 2) - h * w
    if brown_cnt == brown:
        return True
    return False


def solution(brown, yellow):
    answer = []
    carpets = []

    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            carpets.append([i, yellow // i])

    for carpet in carpets:
        if checkCarpet(carpet[0], carpet[1], brown):
            answer.append(carpet[1] + 2)
            answer.append(carpet[0] + 2)

    return answer