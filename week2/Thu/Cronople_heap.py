from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    jobs.sort()
    now = 0
    h = []
    i = 0
    
    while(i < len(jobs)) :
        if now <= jobs[i][0] and not h:
            now = jobs[i][0] + jobs[i][1]
            answer += jobs[i][1]
            i += 1
        else:
            while jobs[i][0] < now:
                heappush(h, [jobs[i][1], jobs[i][0]])
                i += 1
                if i == len(jobs):
                    break
        if h:
            tmp = heappop(h)
            answer += now - tmp[1] + tmp[0]
            now += tmp[0] # jobs[1]
            
    if h:
        while h:
            tmp = heappop(h)
            answer += now - tmp[1] + tmp[0]
            now += tmp[0] # jobs[1]

    print(answer)
    return answer // len(jobs)