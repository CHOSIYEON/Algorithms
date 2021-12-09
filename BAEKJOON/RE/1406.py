import sys
from collections import deque
input = sys.stdin.readline

left_queue = deque()
right_queue = deque()

arr = input().rstrip('\n')
n = int(input())

for i in arr:
    left_queue.append(i)

for i in range(n):
    cmd = input().split()

    if cmd[0] == 'L':
        if len(left_queue) != 0:
            right_queue.appendleft(left_queue.pop())
    elif cmd[0] == 'D':
        if len(right_queue) != 0:
            left_queue.append(right_queue.popleft())
    elif cmd[0] == 'B':
        if len(left_queue) != 0:
            left_queue.pop()
    elif cmd[0] == 'P':
        left_queue.append(cmd[1])

for i in left_queue+right_queue:
    print(i, end='')