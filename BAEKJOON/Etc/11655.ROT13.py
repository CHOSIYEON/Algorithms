data = input()
answer = ''

for d in data:
    if 97 <= ord(d) < 123:
        if ord(d) + 13 > 122:
            answer += chr(ord(d) - 13)
        else:
            answer += chr(ord(d) + 13)
    elif 65 <= ord(d) < 91:
        if ord(d) + 13 > 90:
            answer += chr(ord(d) - 13)
        else:
            answer += chr(ord(d) + 13)
    else:
        answer += d

print(answer)