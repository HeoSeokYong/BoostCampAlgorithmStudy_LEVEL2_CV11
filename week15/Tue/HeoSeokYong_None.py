def solution(dirs):
    x, y = 0, 0
    visited = set()
    dd = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    
    for dir in dirs:  
        xx = x + dd[dir][0]
        yy = y + dd[dir][1]
        if -5 <= xx <= 5 and -5 <= yy <= 5:
            visited.add((x,y,xx,yy))
            visited.add((xx,yy,x,y))
            x, y = xx, yy
            
    return len(visited)//2