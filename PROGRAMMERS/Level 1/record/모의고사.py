def solution(answers):
    answer = []
    person = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    grade = [0, 0, 0]

    for i in range(3):
        if len(answers) > len(person[i]):
            for j in range(len(answers) - len(person[i])):
                person[i].append(person[i][j])

    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == person[i][j]:
                grade[i] += 1

    for i in range(len(grade)):
        if grade[i] == max(grade):
            answer.append(i + 1)

    answer = sorted(answer)

    return answer