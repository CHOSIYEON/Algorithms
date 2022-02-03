def solution(s):
    answer = len(s)
    length = len(s)

    for i in range(1, length//2 + 1):
        prev = s[:i]
        cnt = 1
        arr = ''
        for j in range(2*i, length + 1, i):
            now = s[j-i:j]
            if prev == now:
                cnt += 1
            else:
                if cnt >= 2:
                    arr += str(cnt)
                arr += prev
                prev = now
                cnt = 1
        if cnt >= 2:
            arr += str(cnt)
        arr += prev
        if length % i != 0:
            arr += s[length//i*i:]

        answer = min(answer, len(arr))

    return answer
