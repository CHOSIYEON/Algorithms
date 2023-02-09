def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        list = array[commands[i][0]-1:commands[i][1]]
        list = sorted(list)
        answer.append(list[commands[i][2]-1])
    return answer