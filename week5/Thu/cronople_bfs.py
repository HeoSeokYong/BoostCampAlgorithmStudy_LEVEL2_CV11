def func(maps, val):
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    new_val = []
    
    for i, j in val:
        cost = maps[i][j]
        
        for xy in range(4):
            if -1 < i+dx[xy] <len(maps) and \
            -1 < j+dy[xy] < len(maps[0]):
                
                if maps[i+dx[xy]][j+dy[xy]] == 1:
                    maps[i+dx[xy]][j+dy[xy]] = cost+1
                    new_val.append((i+dx[xy], j+dy[xy]))
                    
                elif maps[i+dx[xy]][j+dy[xy]] > 1:
                    if maps[i+dx[xy]][j+dy[xy]] > cost+1:
                        maps[i+dx[xy]][j+dy[xy]] = cost+1
                        new_val.append((i+dx[xy], j+dy[xy]))
    return new_val

def solution(maps):
    val = [(0, 0)]
    
    while val:
        val = func(maps, val)
    
    answer = maps[-1][-1]
    
    if answer == 1:
        answer = -1
    return answer