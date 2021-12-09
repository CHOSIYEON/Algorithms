strings = input()
tmp = ''

for i in strings:
    if 97 <= ord(i) <= 122:
        if ord(i) + 13 <= 122:
            tmp += chr(ord(i)+13)
        else:
            tmp += chr(ord(i)-13)
    elif 65 <= ord(i) <= 90:
        if ord(i) + 13 <= 90:
            tmp += chr(ord(i)+13)
        else:
            tmp += chr(ord(i)-13)
    else:
        tmp += i

print(tmp)