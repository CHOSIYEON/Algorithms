# 시간초과
# import sys
# input = sys.stdin.readline
#
# sentence = list(sys.stdin.readline().rstrip('\n'))
# n = int(input())
# n2 = n
# cursor = len(sentence) + 1
#
# for i in range(n2):
#     command = sys.stdin.readline().split()
#
#     if command[0] == 'L':
#         if cursor != 1:
#             cursor -= 1
#     elif command[0] == 'D':
#         if cursor != n+1:
#             cursor += 1
#     elif command[0] == 'B':
#         if cursor != 1:
#             del sentence[cursor-2]
#             cursor -= 1
#             n -= 1
#     elif command[0] == 'P':
#         sentence.insert(cursor-1, command[1])
#         cursor += 1
#         n += 1
#
# for i in sentence:
#     print(i, end='')

import sys
input = sys.stdin.readline

stackLeft = list(input().rstrip())
stackRight = list()
n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == 'L' and stackLeft:
        stackRight.append(stackLeft.pop())
    elif command[0] == 'D' and stackRight:
        stackLeft.append(stackRight.pop())
    elif command[0] == 'B' and stackLeft:
        stackLeft.pop()
    elif command[0] == 'P':
        stackLeft.append(command[1])

print(''.join(stackLeft) + ''.join(list(reversed(stackRight))))
