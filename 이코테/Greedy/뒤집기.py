s = list(map(int, input()))
count = {0: 0, 1: 0}
prev = s[0]

if 0 in s and 1 in s:
    for i in range(1, len(s)):
        if prev != s[i]:
            count[prev] += 1
            prev = s[i]

    if prev == s[-1]:
        count[prev] += 1

min_value = min(count.values())
print(min_value)