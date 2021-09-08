# 효율성 테스트 통과 못함
def solution(info, query):
    answer = []
    for i in query:
        cmd = list(i.split())
        check = [1] * len(info)
        for j in range(8):
            if j%2== 0:
                for m in range(len(info)):
                    infos = list(info[m].split())
                    if check[m]:
                        if cmd[j] == '-':
                            pass
                        else:
                            if infos[j//2] != cmd[j]:
                                check[m] = 0
            elif j==7:
                for m in range(len(info)):
                    infos = list(info[m].split())
                    if check[m]:
                        if cmd[j] == '-':
                            pass
                        else:
                            if int(infos[4]) < int(cmd[j]):
                                check[m] = 0
        answer.append(check.count(1))
    return answer