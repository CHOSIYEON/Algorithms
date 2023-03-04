# https://johnyejin.tistory.com/127

def rotation(arr):
    n = len(arr)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = arr[i][j]
    return rotated

def check(startX, startY, key, lock, start, end, expendSize):
    board = [[0] * expendSize for _ in range(expendSize)]

    # board 에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            board[startX + i][startY + j] += key[i][j]

    # board 에 lock 추가하면서 기존 값이랑 더하기
    for i in range(start, end):
        for j in range(start, end):
            board[i][j] += lock[i - start][j - start]
            if board[i][j] != 1:
                return False

    return True

def solution(key, lock):
    start = len(key) - 1  # board에서 lock의 시작 지점
    end = start + len(lock)  # board에서 lock이 끝나는 지점
    expendSize = len(lock) + start * 2  # board 배열의 크기

    # lock 은 고정시키고, key 값을 돌려가며 확인
    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, start, end, expendSize):
                    return True
        key = rotation(key)

    return False

