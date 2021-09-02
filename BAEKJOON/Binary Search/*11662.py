# 삼분탐색
# https://velog.io/@bobsiunn/Search-11662번-민호와-강호-24일차
import sys
import math
input = sys.stdin.readline

x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())

def minho(p):
    return [x1 + (x2 - x1) * (p/100), y1 + (y2 - y1) * (p/100)]

def kangho(p):
    return [x3 + (x4 - x3) * (p/100), y3 + (y4 - y3) * (p/100)]

def dist(x1, y1, x2, y2):
    return math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

fp = 0
lp = 100

length =  math.sqrt(pow(10000, 2) + pow(10000, 2))

while(lp-fp >= 1e-7):
    p = (fp*2 + lp)/3
    q = (fp + lp*2)/3

    m_p = minho(p)
    m_q = minho(q)
    k_p = kangho(p)
    k_q = kangho(q)

    dist1 = dist(m_p[0], m_p[1], k_p[0], k_p[1])
    dist2 = dist(m_q[0], m_q[1], k_q[0], k_q[1])

    length = min(length, min(dist1, dist2))

    if(dist1 >= dist2):
        fp = p
    else:
        lp = q

print('%.10f' %length)
