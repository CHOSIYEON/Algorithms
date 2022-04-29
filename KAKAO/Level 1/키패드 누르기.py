def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    pos = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1],
           6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}

    for i in numbers:
        if i in [1, 4, 7]:
            left = pos[i]
            answer += 'L'
        elif i in [3, 6, 9]:
            right = pos[i]
            answer += 'R'
        else:
            distance_l = abs(pos[i][0] - left[0]) + abs(pos[i][1] - left[1])
            distance_r = abs(pos[i][0] - right[0]) + abs(pos[i][1] - right[1])
            if distance_l > distance_r:
                right = pos[i]
                answer += 'R'
            elif distance_l < distance_r:
                left = pos[i]
                answer += 'L'
            else:
                if hand == 'left':
                    answer += 'L'
                    left = pos[i]
                else:
                    answer += 'R'
                    right = pos[i]
    return answer