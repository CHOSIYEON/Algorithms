from collections import Counter

data = Counter(input().lower())
data = sorted(data.items(), key=lambda x: -x[1])

if len(data) >= 2:
    if data[0][1] == data[1][1]:
        print("?")
        exit()

print(data[0][0].upper())