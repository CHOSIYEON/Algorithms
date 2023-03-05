n = list(map(int, list(input())))

if sum(n[:len(n) // 2]) == sum(n[len(n) // 2:]):
    print("LUCKY")
else:
    print("READY")