def solution(N, stages):
    answer = [[i, 0] for i in range(N+1)]
    stage = [0 for i in range(N+2)]
    max_stage = max(stages)
    for i in range(1, N+2):
        stage[i] = stages.count(i)
    for i in range(1, N+1):
        if i > max_stage:
            answer[i][1] = 0
        else:
            if stage[i] == 0:
                answer[i][1] = 0
            else:
                answer[i][1] = stage[i]/sum(stage[i:])
    answer = answer[1:]
    answer = sorted(answer, key = lambda x:x[1], reverse = True)
    answer = [x[0] for x in answer]
    return answer