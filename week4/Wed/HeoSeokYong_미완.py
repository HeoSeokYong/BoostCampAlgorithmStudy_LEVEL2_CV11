min_dist=0

def brute(visited, weak, dist):
    min_dist = 0
    
    # for i in range(len(dist)):
        
        
def solution(n, weak, dist):
    answer = 0
    
    dist.reverse()
    
    visited = [False] * len(weak)
    
    sett = []
    for d in dist:
        for w in weak:
            tmp = [x for x in weak if w <= x <= w+d]
            if w+d > n:
                tmp += [x for x in weak if x <= w+d-n]
            sett.append(set(tmp))
            print(sett)

        
        
    
    return answer