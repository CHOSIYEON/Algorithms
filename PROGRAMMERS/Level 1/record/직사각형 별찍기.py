a, b = map(int, input().strip().split(' '))
stars = ''
for i in range(a):
    stars += '*'
for i in range(b):
    print(stars)