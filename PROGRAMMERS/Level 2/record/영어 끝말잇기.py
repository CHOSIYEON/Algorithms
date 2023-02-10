import math

def solution(n, words):
    usedWords = []

    for idx, word in enumerate(words):
        if word in usedWords or (idx >= 1 and words[idx - 1][-1] != word[0]):
            return [idx % n + 1, math.ceil((idx + 1) / n)]

        usedWords.append(word)

    return [0, 0]