import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    cmds = list(map(str, input().split()))

    if len(cmds) == 1:
        if cmds[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        cmd, x = cmds[0], int(cmds[1])

        if cmd == 'add':
            s.add(x)
        elif cmd == 'remove':
            s.discard(x)
        elif cmd == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
        elif cmd == 'check':
            if x in s:
                print(1)
            else:
                print(0)