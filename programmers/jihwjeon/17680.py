from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cache = deque([])
    
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if cacheSize != 0:
                if len(cache) == cacheSize:
                    cache.popleft()
                cache.append(city)
            answer += 5
    
    return answer
