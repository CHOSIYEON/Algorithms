import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    queue = []
    sum_time, prev_time, length = 0, 0, len(food_times)

    for idx, time in enumerate(food_times):
        heapq.heappush(queue, (time, idx + 1))

    while sum_time + ((queue[0][0] - prev_time) * length) <= k:
        now = heapq.heappop(queue)[0]
        sum_time += ((now - prev_time) * length)
        length -= 1
        prev_time = now

    queue = sorted(queue, key=lambda x: x[1])

    return queue[(k - sum_time) % length][1]

