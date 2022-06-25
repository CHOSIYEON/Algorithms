def solution(n, left, right):
    start_row, end_row = left // n, right // n
    start_idx, end_idx = left % n, left % n + right - left
    data = [[x + 1 for _ in range(n)] for x in range(start_row, end_row + 1)]
    temp = []

    for i in range(len(data)):
        for j in range(start_row + i + 1, n):
            data[i][j] = data[i][j - 1] + 1

    for d in data:
        temp.extend(d)

    answer = temp[start_idx:end_idx + 1]
    return answer

# 시간 초과
def solution(n, left, right):
    answer = []
    data = [[0 for _ in range(n)] for _ in range(n)]
    data2 = []

    for i in range(1, n + 1):
        for x in range(i):
            for y in range(i):
                if not data[x][y]:
                    data[x][y] = i

    for d in data:
        data2.extend(d)

    answer = data2[left:right + 1]

    return answer

# 시간초과
def solution(n, left, right):
    answer = []
    data = [[x + 1 for _ in range(n)] for x in range(n)]
    data2 = []

    for i in range(n):
        for j in range(i + 1, n):
            data[i][j] = data[i][j - 1] + 1

    for d in data:
        data2.extend(d)

    answer = data2[left:right + 1]

    return answer