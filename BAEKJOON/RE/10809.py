n = list(input())
alpa = [chr(i) for i in range(97, 123)]

for i in alpa:
    if i in n:
        print(n.index(i), end=' ')
    else:
        print(-1, end=' ')