# 효율성 통과 못함 (1, 2, 3)
def solution(words, queries):
    answer = []
    words.sort(key=lambda x: len(x))

    for query in queries:
        count = 0
        for word in words:
            if len(word) < len(query):
                continue

            if len(word) > len(query):
                break

            for i in range(len(word)):
                if query[i] != word[i] and query[i] != '?':
                    break
            else:
                count += 1

        answer.append(count)

    return answer


## 이코테
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)

    return right_index - left_index


def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        if query[0] != '?':
            res = count_by_range(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(query)], query[::-1].replace('?', 'a'),
                                 query[::-1].replace('?', 'z'))

        answer.append(res)

    return answer

# 다시
from bisect import bisect_left, bisect_right
from collections import defaultdict


def count_value(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)

    return right_index - left_index


def solution(words, queries):
    answer = []
    array = defaultdict(list)
    reversed_array = defaultdict(list)

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for key in array.keys():
        array[key].sort()
        reversed_array[key].sort()

    for query in queries:
        if query[0] == '?':
            count = count_value(reversed_array[len(query)], query[::-1].replace('?', 'a'),
                                query[::-1].replace('?', 'z'))
        else:
            count = count_value(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))

        answer.append(count)
    return answer