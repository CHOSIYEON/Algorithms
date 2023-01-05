def solution(my_string):
    return sorted(map(int, filter(lambda x: x.isdigit(), my_string)))