def solution(dirs):
    sign = {"U": (1, 0), "L": (0,-1), "R":(0,1), "D":(-1,0)} # y, x
    walked = {}
    st = (0,0)
    for s in dirs: 
        vy, vx = sign[s]
        newy = st[0] + vy
        newx = st[1] + vx
        if newy < -5 or newy > 5 or newx < -5 or newx > 5: 
            continue
        walked[(newy,newx,st[0],st[1])] = 1
        walked[(st[0],st[1],newy,newx)] = 1
        st = (newy, newx)
    return (len(walked)/2)
