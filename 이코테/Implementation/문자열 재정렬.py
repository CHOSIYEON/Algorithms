s = list(input())
arr = []
num = 0

# for i in s:
#     if 49 <= ord(i) <= 57:
#         num += int(i)
#     else:
#         arr.append(i)
#
# print(''.join(sorted(arr)), end='')
# print(num)

for i in s:
    if i.isalpha():
        arr.append(i)
    else:
        num += int(i)

print(''.join(sorted(arr)), end='')
print(num)