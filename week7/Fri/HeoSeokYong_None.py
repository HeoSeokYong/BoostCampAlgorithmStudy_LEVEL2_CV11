def solution(n, stations, w):
    answer = 0
    rng = 2*w + 1
    start = 0
    if stations[-1]+w < n:
        stations.append(n+w+1)
    
    for s in stations:
        tmp = s - w - start - 1
        div, mod = divmod(tmp, rng)
        answer += div
        if mod > 0:
            answer += 1
        start = s + w
        
    return answer