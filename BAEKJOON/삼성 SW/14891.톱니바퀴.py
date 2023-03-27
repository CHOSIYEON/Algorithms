import sys
input = sys.stdin.readline
from collections import deque

def cal_left(idx, check, direction):
    if idx == 0:
        return

    if gear[idx][6] != gear[check][2]:
        need_rotate.append((check, direction * (-1)))
        cal_left(idx - 1, check - 1, direction * (-1))

def cal_right(idx, check, direction):
    if idx == 3:
        return

    if gear[idx][2] != gear[check][6]:
        need_rotate.append((check, direction * (-1)))
        cal_right(idx + 1, check + 1, direction * (-1))

gear = [deque(map(int, input().rstrip())) for _ in range(4)]
k = int(input())
answer = 0

for _ in range(k):
    need_rotate = []
    g, d = map(int, input().split())
    need_rotate.append((g - 1, d))

    cal_left(g - 1, g - 2, d)
    cal_right(g - 1, g, d)

    for idx, direction in need_rotate:
        gear[idx].rotate(direction)

for i in range(4):
    if gear[i][0] == 1:
        answer += pow(2, i)

print(answer)