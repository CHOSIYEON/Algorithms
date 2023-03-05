def solution(s):
    answer = 1e9
    length = len(s)

    if length == 1:
        return 1

    for i in range(1, length // 2 + 1):
        prev = s[:i]
        count = 0
        comp = ''
        for j in range(0, length, i):
            now = s[j: j + i]

            if prev == now:
                count += 1
            else:
                if count > 1:
                    comp += str(count)
                comp += prev
                prev = now
                count = 1

        if count > 1:
            comp += str(count)
        comp += now
        answer = min(answer, len(comp))
        
    return answer