def solution(babblings):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]

    for babbling in babblings:
        while len(babbling) > 1:
            if babbling[:2] in can_speak:
                babbling = babbling[2:]
            elif babbling[:3] in can_speak:
                babbling = babbling[3:]
            else:
                break
        if not len(babbling):
            answer += 1
    return answer