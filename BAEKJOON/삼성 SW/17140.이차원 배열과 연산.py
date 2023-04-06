def sort_row():
    length = len(data[0])
    max_length = 0

    for i in range(len(data)):
        row = {}
        for j in range(length):
            if data[i][j] == 0:
                continue

            if data[i][j] in row.keys():
                row[data[i][j]] += 1
            else:
                row[data[i][j]] = 1

        row = sorted(row.items(), key= lambda x: (x[1], x[0]))
        temp = []

        for j in range(len(row)):
            temp.append(row[j][0])
            temp.append(row[j][1])

        temp = temp[:100]

        max_length = max(max_length, len(temp))
        data[i] = temp

    for i in range(len(data)):
        while len(data[i]) != max_length:
            data[i].append(0)

r, c, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(3)]
answer = 0

for i in range(101):
    row, column = len(data), len(data[0])

    if 0 <= r - 1 < row and 0 <= c - 1 < column:
        if data[r - 1][c - 1] == k:
            print(i)
            break

    if row >= column:
        sort_row()
    else:
        data = list(map(list, zip(*data)))
        sort_row()
        data = list(map(list, zip(*data)))
else:
    print(-1)