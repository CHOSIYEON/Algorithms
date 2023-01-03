def solution(num_list):
    return [sum(list(map(lambda x: x % 2 == 0, num_list))), sum(list(map(lambda x: x % 2 != 0, num_list)))]

####

def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        answer[i % 2] += 1
    return answer