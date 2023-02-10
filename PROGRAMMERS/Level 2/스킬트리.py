def isPossible(skill, skill_tree):
    now = 0
    for s in skill_tree:
        if s in skill:
            if now >= skill.index(s):
                now = skill.index(s) + 1
            else:
                return False

    return True


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        if isPossible(skill, skill_tree):
            answer += 1

    return answer

##########################

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        check = ''

        for s in skill_tree:
            if s in skill:
                check += s

        if check == skill[0:len(check)]:
            answer += 1

    return answer