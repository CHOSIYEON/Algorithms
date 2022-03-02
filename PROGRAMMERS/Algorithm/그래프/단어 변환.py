from collections import deque


def solution(begin, target, words):
    visited = [False] * len(words)

    if not target in words:
        return 0

    queue = deque()
    queue.append([begin, 0])

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt

        for i in range(len(words)):
            tmp = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    visited[i] = True
                    queue.append([words[i], cnt + 1])