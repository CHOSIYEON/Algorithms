def get_time(line):
    line = list(line.split())
    hour, minute, second, millisecond = int(line[1][:2]), int(line[1][3:5]), int(line[1][6:8]), int(line[1][9:])
    t = float(line[2][:-1]) * 1000 - 1
    endTime = (hour * 60 * 60 * 1000) + (minute * 60 * 1000) + (second * 1000) + millisecond
    startTime = endTime - t

    return (startTime, endTime)

def solution(lines):
    answer = 0
    times = []

    for line in lines:
        times.append(get_time(line))

    for i in range(len(times)):
        cnt = 0
        for j in range(i, len(times)):
            if times[i][1] + 1000 > times[j][0]:
                cnt += 1

        answer = max(answer, cnt)
    return answer