import heapq

INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(maps):
    
    new_maps = []
    
    for i in maps:
        n = [j if j==0 else INF for j in i]
        new_maps.append(n)
    
    q = []
    heapq.heappush(q, (1, (0,0)))
    new_maps[0][0] = 1
    
    while q :
        dist, now = heapq.heappop(q)
        
        for i in range(4):
            new_x = now[0] + dx[i]
            new_y = now[1] + dy[i]
            
            # 맵 밖으로 벗어날 경우
            if new_x<0 or new_x>=len(new_maps) or new_y<0 or new_y>=len(new_maps[0]):
                continue
            
            # 벽일 경우
            if new_maps[new_x][new_y]==0:
                continue

            cost = dist + 1
            if cost < new_maps[new_x][new_y]:
                new_maps[new_x][new_y] = cost
                heapq.heappush(q, (cost, (new_x, new_y)))
    
    if new_maps[-1][-1] != INF:
        answer = new_maps[-1][-1]
    else:
        answer = -1
        
    return answer