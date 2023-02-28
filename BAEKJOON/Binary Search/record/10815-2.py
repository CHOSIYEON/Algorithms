import sys
input = sys.stdin.readline

def check(num):
    low = 0
    high = len(cards) - 1

    while low <= high:
        mid = (low + high) // 2

        if num == cards[mid]:
            return True
        elif num < cards[mid]:
            high = mid - 1
        elif num > cards[mid]:
            low = mid + 1

    return False


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
cards2 = list(map(int, input().split()))

cards.sort()

for i in cards2:
    if check(i):
        print(1, end=' ')
    else:
        print(0, end=' ')