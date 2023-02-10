def solution(s):
    cnt, cnt_zero = 0, 0

    while len(s) != 1:
        cnt += 1
        cnt_zero += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s)))[2:]

    return [cnt, cnt_zero]