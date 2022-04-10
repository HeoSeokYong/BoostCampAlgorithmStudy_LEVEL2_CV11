def solution(n, times):
    times.sort()
    answer = 0
    left = 1
    right = n * times[-1]
    
    while left <= right:
        mid = (left+right) // 2
        check = 0
        for t in times:
            check += mid // t
            if check >= n:
                answer = mid
                right = mid - 1
                break
        if check < n:
            left = mid + 1
    
    return answer