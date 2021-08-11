num = int(input())
answer = ''

if not num:
    print('0')
    exit()
else:
    while num:
        if num % -2:
            answer = '1' + answer
            num = num // -2 + 1
        else:
            answer = '0' + answer
            num = num // -2

print(answer)
