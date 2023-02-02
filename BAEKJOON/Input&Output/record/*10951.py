import sys

lines = sys.stdin.readlines()

for line in lines:
    a, b = map(int, line.split())
    print(a+b)

# ////////////////////////////////////////

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break

