from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()

        if len(most_ordered) == 0:
            continue

        max_value = most_ordered[0][1]

        for key, value in most_ordered:
            if value > 1 and value == max_value:
                answer.append(''.join(key))

    return sorted(answer)


# from itertools import combinations
# from collections import defaultdict
#
# def solution(orders, course):
#     answer = []
#     order_info = defaultdict(int)
#
#     for order in orders:
#         order = ''.join(sorted(list(order)))
#         for i in course:
#             if len(order) >= i:
#                 temp = list(combinations(order, i))
#                 for j in temp:
#                     order_info[''.join(j)] += 1
#
#     order_info = dict(sorted(order_info.items(), key=lambda x: -x[1]))
#
#     for i in course:
#         max_value = -1e9
#         max_temp = []
#         for key in order_info.keys():
#             if len(key) == i and order_info[key] >= 2:
#                 if order_info[key] > max_value:
#                     max_temp = [key]
#                     max_value = order_info[key]
#                 elif order_info[key] == max_value:
#                     max_temp.append(key)
#
#         for i in max_temp:
#             answer.append(i)
#
#     answer.sort()
#
#     return answer
