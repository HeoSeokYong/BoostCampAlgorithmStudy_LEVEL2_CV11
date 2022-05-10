def solution(n, edge):
    dist = [0, 0] + [20001 for _ in range(n-1)]
    nlist = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    for v1, v2 in edge:
        nlist[v1].append(v2)
        nlist[v2].append(v1)
    
    q = [(nlist[1], 0)]

    while q:
        path = q.pop(0)
        for p in path[0]:
            if not visited[p]:
                visited[p] = True
                dist[p] = min(dist[p], path[1]+1)
                q.append((nlist[p], path[1]+1))
    
    return dist.count(max(dist))