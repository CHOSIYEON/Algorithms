# import sys
# from collections import Counter
# input = sys.stdin.readline
#
# buy = int(input())
# m, n = map(int, input().split())
# pizza_a = [int(input()) for _ in range(m)]
# pizza_b = [int(input()) for _ in range(n)]
#
# sum_a = []
# sum_b = []
#
# sum_a.append(0)
# sum_b.append(0)
# sum_a.append(sum(pizza_a))
# sum_b.append(sum(pizza_b))
#
# for i in range(1, m):
#     for j in range(m):
#         if j+i > m:
#             sum_a.append(sum(pizza_a[j:]) + sum(pizza_a[:j-i+1]))
#         else:
#             sum_a.append(sum(pizza_a[j:j+i]))
#
# for i in range(1, n):
#     for j in range(n):
#         if j+i > n:
#             sum_b.append(sum(pizza_b[j:]) + sum(pizza_b[:j-i+1]))
#         else:
#             sum_b.append(sum(pizza_b[j:j+i]))
#
# c = Counter(sum_b)
# ans = 0
#
# for i in sum_a:
#     ans += c[buy-i]
#
# print(ans)
