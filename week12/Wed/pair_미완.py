def solution(n, s, a, b, fares):
    '''
        dfs, 다익스트라, 플로이드 마샬
    '''
    answer = 0
    path = {}
    for i in range(1, n+1):
        path[i] = []
    for q,w,e in fares:
        path[q].append([w,e])
        path[w].append([q,e])
    print(path)
    return answer