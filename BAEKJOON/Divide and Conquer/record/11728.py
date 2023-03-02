import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list_n = list(map(int, input().split()))
list_m = list(map(int, input().split()))
result = sorted(list_n + list_m)
print(' '.join(list(map(str, result))))
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# list_n = list(map(int, input().split()))
# list_m = list(map(int, input().split()))
# result = []
#
# while len(list_n)>0 and len(list_m):
#     if list_n[0] <= list_m[0]:
#         result.append(list_n.pop(0))
#     else:
#         result.append(list_m.pop(0))
#
# if len(list_n):
#     for i in list_n:
#         result.append(i)
# if len(list_m):
#     for i in list_m:
#         result.append(i)
#
# result = list(map(str, result))
# print(' '.join(result))
