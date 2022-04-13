from collections import deque

def solution(gems):  
    p0 = 0
    p1 = 0
    last = len(gems) - 1
    cat_gems = len(set(gems))
    save = []
    gem_q = deque()
    len_g = 0
    
    while p1 <= last:
        if gems[p1] not in gem_q:
            len_g += 1
        gem_q.append(gems[p1])
        
        if len_g == cat_gems:
            while True:
                if gem_q[0] in gems[p0+1:p1]:
                    gem_q.popleft()
                    p0 += 1
                else:
                    save.append([p0, p1])
                    gem_q.popleft()
                    p0 += 1
                    break
            len_g -= 1
        p1 += 1
    
    answer = [0, 100000]
    for s in save:
        if s[1]-s[0] < answer[1] - answer[0]:
            answer = s
            
    return [answer[0]+1, answer[1]+1]