def solution(numbers, hand):
    answer = ''
    location_l = 10
    location_r = 12
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    for i in numbers:
        if i % 3 == 0:
            location_r = i
            answer += 'R'
        elif i % 3 == 1:
            location_l = i
            answer += 'L'
        elif i % 3 == 2:
            distance_l = abs(i-location_l) // 3 + abs(i-location_l) % 3
            distance_r = abs(i-location_r) // 3 + abs(i-location_r) % 3
            if distance_l > distance_r:
                location_r = i
                answer += 'R'
            elif distance_l < distance_r:
                location_l = i
                answer += 'L'
            elif distance_l == distance_r:
                if hand == 'right':
                    location_r = i
                    answer += 'R'
                elif hand == 'left':
                    location_l = i
                    answer += 'L'
    return answer