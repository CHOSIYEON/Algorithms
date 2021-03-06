import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

blue_count, white_count = 0, 0

def dividePaper(x, y, n):
    global blue_count, white_count

    check_color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check_color != graph[i][j]:
                check_color = -1
                break

    if check_color == -1:
        n = n // 2
        dividePaper(x, y, n)
        dividePaper(x + n, y, n)
        dividePaper(x, y + n, n)
        dividePaper(x + n, y + n, n)
    elif check_color == 0:
        white_count += 1
    elif check_color == 1:
        blue_count += 1

dividePaper(0, 0, n)
print(white_count)
print(blue_count)