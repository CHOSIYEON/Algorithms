n = int(input())
turn = -1

while n > 3:
    n -= 3
    turn *= (-1)

if n % 2 == 1:
    turn *= (-1)

if turn == -1:
    print("CY")
else:
    print("SK")