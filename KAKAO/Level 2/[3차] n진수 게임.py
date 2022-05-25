def convert(num, base):
    tmp = '0123456789ABCDEF'
    q, r = num // base, num % base
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def solution(base, t, m, p):
    answer = ''
    numbers = ''
    num = 0

    while len(numbers) < t * m:
        numbers += str(convert(num, base))
        num += 1

    for i in range(p - 1, t * m, m):
        answer += numbers[i]

    return answer
    # return numbers[p-1:t*m:m]


######################

def solution(base, t, m, p):
    numbers = ''
    num = 0

    while len(numbers) < t * m:
        numbers += str(convert(num, base))
        num += 1

    return numbers[p-1:t*m:m]