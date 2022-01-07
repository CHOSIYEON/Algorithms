from itertools import combinations

def make_code():
    result = []

    for i in list(combinations(chars, l)):
        vowel_cnt = 0
        consonant_cnt = 0
        for j in i:
            if j in vowels:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if vowel_cnt > 0 and consonant_cnt > 1:
            result.append(''.join(i))

    return result

l, c = map(int, input().split())
chars = list(map(str, input().split()))
chars.sort()

vowels = {'a', 'i', 'o', 'u', 'e'}

for i in make_code():
    print(i)