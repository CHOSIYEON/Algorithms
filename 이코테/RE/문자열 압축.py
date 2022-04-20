def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1, 1):
        previous = s[:i]
        cnt = 0
        result = ''
        for j in range(0, len(s), i):
            now = s[j:j + i]
            if previous == now:
                cnt += 1
            else:
                if cnt >= 2:
                    result += str(cnt) + previous
                else:
                    result += previous
                previous = now
                cnt = 1

        if cnt >= 2:
            result += str(cnt) + previous
        else:
            result += previous

        answer = min(answer, len(result))

    return answer