import heapq

def solution(jobs):
    heap = []
    len_j = len(jobs)
    
    jobs.sort()
    
    timee = jobs[0][0]
    cur = 0
    answer = 0
    
    heapq.heappush(heap, jobs.pop(0)[::-1])
    
    while heap:
        hpop = heapq.heappop(heap)
        timee += hpop[0]
        cur += hpop[1]
        answer += timee - hpop[1]

        if jobs:
            tmp = [x for x in jobs if x[0] <= timee]
            if len(tmp) != 0:
                for t in tmp:
                    heapq.heappush(heap, t[::-1])
                    jobs.remove(t)

            if not heap:
                if timee < jobs[0][0]:
                    timee = jobs[0][0]
                heapq.heappush(heap, jobs.pop(0)[::-1])
                
    return answer // len_j