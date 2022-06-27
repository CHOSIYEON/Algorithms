from collections import defaultdict

def check(skill_tree):
    now = 1
    for s in skill_tree:
        if skill_info[s]:
            if now != skill_info[s]:
                return False
            now += 1
    return True


def solution(skill, skill_trees):
    answer = 0
    global skill_info
    skill_info = defaultdict(int)

    for idx, s in enumerate(skill):
        skill_info[s] = idx + 1

    for skill_tree in skill_trees:
        if check(skill_tree):
            answer += 1

    return answer


##
def check(skill_tree, skill):
    now = 0
    for s in skill_tree:
        if s in skill:
            if skill.index(s) == now:
                now += 1
            else:
                return False
    return True


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        if check(skill_tree, skill):
            answer += 1

    return answer