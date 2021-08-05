import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    line = str(input().strip())
    cmd = ''
    num = 0

    if line.count(' ') != 0:
        cmd, num = line.split()
    else:
        cmd = line

    if cmd == 'push':
        arr.append(int(num))
    elif cmd == 'pop':
        if len(arr) != 0:
            print(arr[-1])
            arr = arr[:-1]
        else:
            print(-1)
    elif cmd == 'size':
        print(len(arr))
    elif cmd == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(arr) != 0:
            print(arr[-1])
        else:
            print(-1)


