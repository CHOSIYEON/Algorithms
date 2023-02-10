## 통과 - deque
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_weight = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while bridge:
        answer += 1
        total_weight -= bridge.popleft()

        if truck_weights:
            if truck_weights[0] + total_weight <= weight:
                total_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)

    return answer


## 5번 시간초과 - deque
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while bridge:
        answer += 1
        bridge.popleft()

        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)

    return answer

## 통과 - 리스트
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while bridge:
        answer += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer


