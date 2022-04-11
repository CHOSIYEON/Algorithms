def solution(s):
    number = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
              'seven': '7', 'eight': '8', 'nine': '9'}
    s = list(s)
    answer = ''
    temp = ''

    for i in s:
        if i.isdigit():
            answer += str(i)
            continue

        temp += i

        if temp in number.keys():
            answer += number[temp]
            temp = ''

    return int(answer)