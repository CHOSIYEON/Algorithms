def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return num * factorial(num-1)

n = int(input())

print(factorial(n))