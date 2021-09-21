n = list(map(int, input()))

if 0 in n and sum(n) % 3 == 0:
    n.sort(reverse=True)
    print(int(''.join(list(map(str,n)))))
else:
    print(-1)