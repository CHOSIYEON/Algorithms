import sys

while True:
    strings = sys.stdin.readline().rstrip('\n')
    up, lo, sp, nu = 0, 0, 0, 0

    if not strings:
        break
    for i in strings:
        if i.isupper():
            up += 1
        elif i.islower():
            lo += 1
        elif i.isdigit():
            nu += 1
        elif i.isspace():
            sp += 1
    print(lo, up, nu, sp, sep=' ')