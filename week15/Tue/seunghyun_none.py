def mover(x,y, dir):
    if dir == 'U':
        nx, ny = x, y-1
    elif dir == 'D':
        nx, ny = x, y+1
    elif dir == 'R':
        nx, ny = x+1, y
    else:
        nx, ny = x-1, y
    return nx, ny

def solution(dirs):
    x,y = 0, 0
    
    t = set()
    t.add((0,0))
    
    for dir in dirs:
        temp_x, temp_y = x, y
        nx, ny = mover(x,y, dir)
        
        if -5<=nx<=5 and -5<=ny<=5: 
            t.add((x,y, nx, ny))
            t.add((nx,ny,x, y))
            x,y = nx, ny

        else: # 범위 밖을 벗어나면 이전 좌표는 그대로, dir만 다음으로.
            x, y = temp_x, temp_y

    return len(t)//2