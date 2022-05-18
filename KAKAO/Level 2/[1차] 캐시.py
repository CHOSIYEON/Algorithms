def solution(cacheSize, cities):
    cache = {}
    cities = [x.lower() for x in cities]
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    for idx, city in enumerate(cities):
        if city in cache.keys():
            cache[city] = idx
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache[city] = idx
                answer += 5
            else:
                minKey = min(cache.keys(), key=lambda x: cache[x])
                cache.pop(minKey)
                cache[city] = idx
                answer += 5

    return answer

####################################################

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cities = [x.lower() for x in cities]
    cache = deque(maxlen=cacheSize)

    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5

    return answer