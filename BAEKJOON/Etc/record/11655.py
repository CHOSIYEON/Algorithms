n = input()

answer = ''

for i in n:
    if i.islower():
        if 97 <= ord(i) + 13 < 123:
            answer += chr(ord(i) + 13)
        else:
            answer += chr(ord(i) - 13)
    elif i.isupper():
        if 65 <= ord(i) + 13 < 91:
            answer += chr(ord(i) + 13)
        else:
            answer += chr(ord(i) - 13)
    else:
        answer += i

print(answer)
