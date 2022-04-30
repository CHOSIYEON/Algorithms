def solution(s):
    arr = ''
    answer = 1e9

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        prev = s[:i]
        count = 1
        for j in range(i, len(s), i):
            now = s[j:j + i]
            if prev == now:
                count += 1
            else:
                if count != 1:
                    arr += str(count) + prev
                else:
                    arr += prev
                prev = now
                count = 1
        if count == 1:
            arr += prev
        else:
            arr += str(count) + prev

        answer = min(answer, len(arr))
        arr = ''

    return answer