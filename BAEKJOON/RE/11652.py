import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    temp = int(input())
    if temp in dic:
        dic[temp] += 1
    else:
        dic[temp] = 1

dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(dic[0][0])
