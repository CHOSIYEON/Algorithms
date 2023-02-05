data = input()

for i in range(97, 123):
    if chr(i) in data:
        print(data.index(chr(i)), end = ' ')
    else:
        print(-1, end = ' ')