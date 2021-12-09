import sys
input = sys.stdin.readline

while True:
    strings = input().rstrip('\n')
    lc, uc, num, sp = 0, 0, 0, 0

    if not strings:
        break

    for i in strings:
        if i.islower():
            lc += 1
        elif i.isupper():
            uc += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            sp += 1

    print(lc, uc, num, sp, sep=' ')

