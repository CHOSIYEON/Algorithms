def solution(scores):
    score_sum = sorted([sum(score) for score in scores], reverse=True)
    return list(map(lambda score: score_sum.index(sum(score)) + 1, scores))