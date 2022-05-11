def solution(n, edge):
    edge_list = [[] for _ in range(n+1)]
    for v in edge:
        a, b = v
        edge_list[a].append(b)
        edge_list[b].append(a)
    
    visited = [False] * (n+1); visited[1] = True
    queue = [edge_list[1]]
    
    while queue:
        temp_list = list()
        for v_list in queue:
            for v in v_list:
                if not visited[v]:
                    visited[v] = True
                    temp_list.append(edge_list[v])
        answer = len(queue)
        queue = temp_list
    
    return answer
