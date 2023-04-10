import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == 'end':
        break

    c1, c2, c3 = False, True, True
    prev, count1, count2 = '', 0, 0

    for i in s:
        if prev == i and prev != 'o' and prev != 'e':
            c3 = False
            break

        if i in ['a', 'e', 'i', 'o', 'u']:
            c1 = True
            count2 = 0
            count1 += 1
        else:
            count1 = 0
            count2 += 1

        if count1 == 3 or count2 == 3:
            c2 = False
            break

        prev = i

    if c1 and c2 and c3:
        print("<" + s + ">" + " is acceptable.")
    else:
        print("<" + s + ">" + " is not acceptable.")


