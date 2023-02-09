def solution(n, m):
    answer = []
    nums = []
    max = 0
    for i in range(1, n + 1):
        if n % i == 0:
            nums.append(i)

    for j in range(1, m + 1):
        if m % j == 0:
            nums.append(j)

    for i in nums:
        if nums.count(i) >= 2:
            max = i

    answer = [max, n * m / max]

    return answer

# def gcdlcm(a, b):
#     c, d = max(a, b), min(a, b)
#     t = 1
#     while t > 0:
#         t = c % d
#         c, d = d, t
#     answer = [c, int(a*b/c)]
#
#     return answer