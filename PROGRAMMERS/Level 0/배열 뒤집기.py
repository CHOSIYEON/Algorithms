def solution(num_list):
    for i in range(len(num_list) // 2 + 1):
        tmp = num_list[i]
        num_list[i] = num_list[len(num_list) - 1 - i]
        num_list[len(num_list) - 1 - i] = tmp

    return num_list

####

def solution(num_list):
    return num_list[::-1]