data = input()
alpha = [0] * 26

for d in data:
    alpha[ord(d) - 97] += 1

print(' '.join([str(x) for x in alpha]))