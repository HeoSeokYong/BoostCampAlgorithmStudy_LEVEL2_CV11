# https://programmers.co.kr/learn/courses/30/lessons/42627#
# 디스크 컨트롤러

import heapq
import math 

def solution(jobs):
    org = jobs.copy()
    jobs = sorted(jobs)
    end = jobs[0][0]
    heap = []
    idx = 0
    answer = 0
    first = jobs.pop(0)
    heapq.heappush(heap, [first[1], first[0]])
    
    while (heap):
        item = heapq.heappop(heap)
        answer += end + item[0] - item[1]
        end += item[0] # 걸리는 시간 더함 
        print(end, answer)
        while (jobs and jobs[0][0] <= end):
            out = jobs.pop(0)
            heapq.heappush(heap, [out[1], out[0]])
        if len(heap) == 0 and jobs:
            out = jobs.pop(0)
            end = out[0]
            heapq.heappush(heap, [out[1], out[0]])
    print(end, answer)
    answer = math.floor(answer / len(org))
    return answer
