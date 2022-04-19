s = list(map(int, input()))
cnt = [0, 0]
cnt[s[0]] += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt[s[i+1]] += 1

print(min(cnt))