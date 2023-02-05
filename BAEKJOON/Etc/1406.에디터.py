import sys
input = sys.stdin.readline
from collections import deque

queue_l, queue_r = deque(), deque()
data = input().rstrip()
m = int(input())

for d in data:
    queue_l.append(d)

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'L':
        if queue_l:
            queue_r.appendleft(queue_l.pop())
    elif cmd[0] == 'D':
        if queue_r:
            queue_l.append(queue_r.popleft())
    elif cmd[0] == 'B':
        if queue_l:
            queue_l.pop()
    else:
        queue_l.append(cmd[1])

print(''.join(queue_l), end='')
print(''.join(queue_r))