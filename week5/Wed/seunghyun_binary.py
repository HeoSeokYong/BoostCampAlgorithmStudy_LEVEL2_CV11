def solution(n, times):
    answer = 0
    start = 1 
    end = min(times)*n

    while start <= end:
        mid = (start + end) // 2 # 모든 사람이 심사를 받는데 걸리는 시간
        
        result = 0
        
        for t in times:
            result += (mid // t) # 각 심사관이 심사할 수 있는 사람 수
            
        if result >= n: # 조건에 만족하면 answer 업데이트
            answer = mid
            end = mid-1 # 현재보다 최소 시간이 존재하는 확인을 위해 end 업데이트
        else:
            start = mid + 1
    return answer