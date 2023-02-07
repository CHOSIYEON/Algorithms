a, p = map(int, input().split())
prev, d = a, [a]

while True:
    now = 0
    for i in str(prev):
        now += pow(int(i), p)

    prev = now

    if prev in d:
        print(d.index(prev))
        break
    else:
        d.append(prev)
