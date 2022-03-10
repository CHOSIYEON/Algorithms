# 메모제이션, 하향식, 탑다운
# d = [0] * 100
#
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
#
# print(fibo(99))식


# 바텀업, 상향식

d = [0] * 100

d[1] = 1
d[2] = 1

n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])