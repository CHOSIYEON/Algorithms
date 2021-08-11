import sys
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

def validation(num):
    for i in range(2, n+1):
        if isPrime(i):
            if isPrime(num-i):
                print('%d = %d + %d' % (num, i, num - i))
                break

while True:
    n = int(input())

    if n:
        validation(n)
    else:
        break