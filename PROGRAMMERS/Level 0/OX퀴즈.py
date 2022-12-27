def solution(quiz):
    answer = []
    # for q in quiz:
    #     if eval(q[:q.index("=")]) == int(q[q.index("=")+1:]):
    #         answer.append("O")
    #     else:
    #         answer.append("X")
    for q in quiz:
        q = q.replace("=", "==")
        if eval(q):
            answer.append("O")
        else:
            answer.append("X")
    return answer