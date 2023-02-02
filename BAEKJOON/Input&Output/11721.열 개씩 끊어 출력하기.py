data = input()

for i in range(0, len(data), 10):
    if i != len(data) // 10 * 10:
        print(data[i:i + 10])
    else:
        print(data[i:])