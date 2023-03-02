import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in sorted(arr1+arr2):
    print(i, end=' ')