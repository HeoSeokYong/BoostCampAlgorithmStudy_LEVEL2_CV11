from collections import deque 

# answer
def solution(n, stations, w):
    que = []
    ba = 1
    for s in stations: 
        st, ed = s-w, s+w
        if st-ba > 0:
            que.append(st - ba)
        ba = ed+1
    if ba <= n:
        que.append(n+1 - ba)
    answer = 0
    for b in que:
        answer += (b // (2*w+1)) + bool(b%(2*w+1))
    return answer

# fail
def solution1(n, stations, w):
    answer = 0
    
    start = 1
    end = n // 2
    answer = n // (w*2 + 1) + 1
    answer -= len(stations)
    if stations[0] -w <= 1:
        a = stations[0]
        stick = 0
    else : 
        a = 1 + w
        stick = 1
    st = 0
    val = a
    while val <= n: 
        if val + w >= n:
            break
        elif st < len(stations) and val+w >= stations[st] - w:
            val = stations[st]
            st += 1
        else:
            val = val + 2*w + 1
            stick += 1
        # print(val, stick)
        
    return stick
