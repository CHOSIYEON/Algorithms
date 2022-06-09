from collections import deque

def isCorrect(s):
    stack = []
    s = deque(s)

    while s:
        tmp = s.popleft()
        if stack:
            if tmp == ']' and stack[-1] == '[':
                stack.pop()
            elif tmp == '}' and stack[-1] == '{':
                stack.pop()
            elif tmp == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(tmp)
        else:
            stack.append(tmp)

    return True if not stack else False

def solution(s):
    answer = 0

    for i in range(len(s)):
        if isCorrect(s[i:] + s[:i]):
            answer += 1

    return answer