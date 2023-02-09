def solution(n, words):
    answer = []
    check, prev = [words[0]], words[0]

    for i in range(1, len(words)):
        if words[i] in check or prev[-1] != words[i][0]:
            return [i % n + 1, i // n + 1]

        check.append(words[i])
        prev = words[i]

    return [0, 0]