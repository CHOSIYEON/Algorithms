import sys

for line in sys.stdin:
    print(line, end='')

# //////////////////////////////////

print(sys.stdin.read())

# //////////////////////////////////

while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break