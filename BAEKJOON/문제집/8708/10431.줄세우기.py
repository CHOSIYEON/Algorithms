import sys
input = sys.stdin.readline

p = int(input())

for t in range(p):
    data = list(map(int, input().split()))[1:]

    s = [data[0]]
    count = 0

    for i in range(1, len(data)):
        if s[-1] > data[i]:
            for j in range(len(s)):
                if data[i] < s[j]:
                    s.insert(j, data[i])
                    count += (len(s) - j - 1)
                    break

        else:
            s.append(data[i])

    print(str(t + 1) + " " + str(count))
