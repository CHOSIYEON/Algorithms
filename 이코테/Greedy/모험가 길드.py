n = int(input())
people = list(map(int, input().split()))

people.sort(reverse=True)
idx, answer = 0, 0

while idx < n:
    if people[idx] <= len(people[idx:]):
        answer += 1
        idx += people[idx]
    else:
        break

print(answer)