def isPossible(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frames):
    answer = []

    for build_frame in build_frames:
        x, y, a, b = build_frame

        if b == 0:
            answer.remove([x, y, a])

            if not isPossible(answer):
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])

            if not isPossible(answer):
                answer.pop()

    return list(sorted(answer, key=lambda x: (x[0], x[1], x[2])))