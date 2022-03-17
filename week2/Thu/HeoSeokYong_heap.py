import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    len_j = len(jobs)
    tim, answer = jobs[0][0], 0
    heapq.heappush(heap, jobs.pop(0)[::-1])
    while heap:
        hpop = heapq.heappop(heap)
        tim += hpop[0]
        answer += tim - hpop[1]
        if jobs:
            for t in [x for x in jobs if x[0] <= tim]:
                heapq.heappush(heap, jobs.pop(jobs.index(t))[::-1])
            if not heap:
                tim = jobs[0][0]
                heapq.heappush(heap, jobs.pop(0)[::-1])  
    return answer // len_j