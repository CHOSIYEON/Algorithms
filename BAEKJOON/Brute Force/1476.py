e, s, m = map(int, input().split())

if e == s and e == m:
    print(e)
else:
    result = 1
    while True:
       a = result - e
       b = result - s
       c = result - m
       if a%15 == 0 and b%28 ==0 and c%19 == 0:
           print(result)
           break
       else:
           result += 1