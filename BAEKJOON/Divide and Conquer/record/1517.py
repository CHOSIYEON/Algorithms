# import sys
# input = sys.stdin.readline
#
# def division(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]
#
#     left = division(left)
#     right = division(right)
#
#     return merge(left, right)
#
# def merge(left, right):
#     result = []
#     global swap
#     swap = 0
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#                 swap = swap + len(left)
#             else:
#                 result.append(right.pop(0))
#                 swap = swap + len(left) + len(right)
#         elif len(left) > 0:
#             result.append(left.pop(0))
#             swap += len(left)
#         elif len(right) > 0:
#             result.append(right.pop(0))
#             swap = swap + len(left) + len(right)
#     return result
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# division(arr)
# print(swap)
