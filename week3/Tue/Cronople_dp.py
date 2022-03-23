def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        for k in range(len(land[i])):
            land[i][k] += max(land[i-1][:k] + land[i-1][k+1:])
    
    answer = max(land[-1])
    return answer