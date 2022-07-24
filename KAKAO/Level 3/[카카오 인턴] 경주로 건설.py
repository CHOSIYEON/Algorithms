from collections import deque

def solution(board):
    answer = []
    queue = deque()
    INF = int(1e9)
    visited = [[[INF for _ in range(len(board))] for _ in range(len(board))] for _ in range(4)]

    for i in range(4):
        visited[i][0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue.append((0, 0, 0, -1))

    while queue:
        x, y, cost, direction = queue.popleft()

        if x == len(board) - 1 and y == len(board) - 1:
            answer.append(cost)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:
                if direction == -1 or direction == i:
                    new = cost + 100
                else:
                    new = cost + 600

                if visited[i][nx][ny] > new:
                    visited[i][nx][ny] = new
                    queue.append((nx, ny, new, i))

    return min(answer)

# TC 25 통과 X
from collections import deque

def solution(board):
    answer = []
    queue = deque()
    INF = int(1e9)
    visited = [[INF for _ in range(len(board))] for _ in range(len(board))]

    visited[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue.append((0, 0, 0, -1))

    while queue:
        x, y, cost, direction = queue.popleft()

        if x == len(board) - 1 and y == len(board) - 1:
            answer.append(cost)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:
                if direction == -1 or direction == abs(dx[i]):
                    new = cost + 100
                else:
                    new = cost + 600

                if visited[nx][ny] >= new:
                    visited[nx][ny] = new
                    queue.append((nx, ny, new, abs(dx[i])))

    return min(answer)

# TC 11 시간 초과
from collections import deque


def solution(board):
    answer = []
    queue = deque()
    INF = int(1e9)
    visited = [[[INF for _ in range(len(board))] for _ in range(len(board))] for _ in range(4)]

    for i in range(4):
        visited[i][0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue.append((0, 0, 0, -1))

    while queue:
        x, y, cost, direction = queue.popleft()

        if x == len(board) - 1 and y == len(board) - 1:
            answer.append(cost)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:
                if direction == -1 or direction == abs(dx[i]):
                    new = cost + 100
                else:
                    new = cost + 600

                if visited[i][nx][ny] >= new:
                    visited[i][nx][ny] = new
                    queue.append((nx, ny, new, abs(dx[i])))

    return min(answer)