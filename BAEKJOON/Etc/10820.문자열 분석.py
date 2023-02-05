import sys
input = sys.stdin.readline

while True:
    data = input().rstrip('\n')
    lower, upper, number, space = 0, 0, 0, 0

    if not data:
        break

    for d in data:
        if d.islower():
            lower += 1
        elif d.isupper():
            upper += 1
        elif d.isdigit():
            number += 1
        else:
            space += 1

    print('%d %d %d %d'%(lower, upper, number, space))
