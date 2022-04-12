from collections import deque

def solution(maps):
    n = len(maps); m = len(maps[0])
    answer = float('inf')
    
    que = deque()
    que.append([0, 0, 1])
    
    while que:
        x, y, cnt = que.popleft()
        if x == m-1 and y == n-1:
            answer = min(answer, cnt)
            break
            
        if cnt >= answer:
            continue
            
        for i in range(4):
            _x = x + (i//2) * ((-1)**i)
            _y = y + (1 - i//2) * ((-1)**i)

            if _x < 0 or _y < 0 or _x >= m or _y >= n or maps[_y][_x] == 0:
                continue
            maps[_y][_x] = 0
            que.append([_x, _y, cnt+1])
            
    if answer == float('inf'):
        return -1

    return answer