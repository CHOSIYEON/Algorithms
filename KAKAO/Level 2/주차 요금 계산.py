import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    infos = defaultdict(list)

    for record in records:
        time, number, history = record.split()
        infos[number].append(time)

    for key in infos.keys():
        total = 0

        for i in range(0, len(infos[key]), 2):
            if i + 1 < len(infos[key]):
                time = (int(infos[key][i + 1].split(":")[0]) * 60 + int(infos[key][i + 1].split(":")[1])) - (
                            int(infos[key][i].split(":")[0]) * 60 + int(infos[key][i].split(":")[1]))
                total += time
            else:
                time = 1439 - (int(infos[key][i].split(":")[0]) * 60 + int(infos[key][i].split(":")[1]))
                total += time

        if total < fees[0]:
            answer.append((key, fees[1]))
        else:
            fee = math.ceil((total - fees[0]) / fees[2]) * fees[3]
            answer.append((key, fees[1] + fee))

    answer = sorted(answer, key=lambda x: x[0])
    return [x[1] for x in answer]