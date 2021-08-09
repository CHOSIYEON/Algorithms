n = str(input())

for i in range(97, 123):
    if n.count(chr(i)) > 0:
        print(n.index(chr(i)))
    else:
        print(-1)