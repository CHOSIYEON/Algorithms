def solution(rows, columns, queries):
    answer = []
    data = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    for query in queries:
        query = [x - 1 for x in query]
        x1, y1, x2, y2 = query
        tmp = data[x1][y1]
        small = tmp

        for i in range(x1 + 1, x2 + 1):
            data[i - 1][y1] = data[i][y1]
            small = min(small, data[i][y1])

        for i in range(y1 + 1, y2 + 1):
            data[x2][i - 1] = data[x2][i]
            small = min(small, data[x2][i])

        for i in range(x2 - 1, x1 - 1, -1):
            data[i + 1][y2] = data[i][y2]
            small = min(small, data[i][y2])

        for i in range(y2 - 1, y1 - 1, -1):
            data[x1][i + 1] = data[x1][i]
            small = min(small, data[x1][i])

        data[x1][y1 + 1] = tmp
        answer.append(small)

    return answer