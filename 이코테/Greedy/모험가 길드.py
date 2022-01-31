n = int(input())
people = list(map(int, input().split()))
tmp = []
ans = 0

people.sort(reverse=True)

while True:
    if people:
        person = people.pop()
        tmp.append(person)
    else:
        break

    if person <= len(tmp):
        ans += 1
        tmp = []

print(ans)

# people.sort()
#
# ans = 0
# cnt = 0
#
# for i in people:
#     cnt += 1
#     if cnt >= i:
#         ans += 1
#         cnt = 0
#
# print(ans)
