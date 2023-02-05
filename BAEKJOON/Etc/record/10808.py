# from collections import Counter
#
# n = str(input())
# count = Counter(n)
# count2 = Counter('abcdefghijklmnopqrstuvwxyz')
#
# count = count + count2
# count = sorted(count.items())
#
# for i in range(len(count)):
#     print(count[i][1]-1, end=' ')

n = str(input())

for i in range(97, 123):
    print(n.count(chr(i)), end=' ')
