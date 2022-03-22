def solution(land):
    '''
    항상 4칸
    연속해서 같은 열을 밟으면 안됨.
    1~마지막 행까지, 현재 행을 [이전 행+현재 행의 최대값]으로 업데이트
    
    아래 코드는 처음 접근했던 방법. 통과는 했으나, 재구성한 리스트에서 최대값을 찾는 다른 팀원들의 풀이 방식이 훨씬 깔끔한듯.
    '''
    
    for i in range(1, len(land)):
        for j in range(4):
            max_ = 0
            for k in range(4):
                if j==k:
                    continue
                max_ = max(max_, land[i-1][k])
                
            land[i][j] += max_
    return max(land[-1])
