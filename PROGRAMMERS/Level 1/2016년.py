def solution(a, b):
    answer = ''
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(1, a):
        total += days[i - 1]
    total += b
    total %= 7

    answer = day[total - 1]

    return answer