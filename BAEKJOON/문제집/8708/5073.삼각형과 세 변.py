while True:
    data = list(map(int, input().split()))
    data.sort()

    if data.count(0) == 3:
        break

    if data[0] + data[1] <= data[2]:
        print("Invalid")
        continue

    if data[0] == data[1] and data[1] == data[2]:
        print("Equilateral")
    elif (data[0] == data[1] and data[1] != data[2]) or (data[0] != data[1] and data[1] == data[2]):
        print("Isosceles")
    else:
        print("Scalene")
