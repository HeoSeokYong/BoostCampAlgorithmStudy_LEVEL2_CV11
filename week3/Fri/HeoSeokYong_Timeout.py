import copy
  
M, N, H = map(int, input().split())
tmts = []

for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(input().split())
    tmts.append(tmp)

# day=0
# M,N,H = 5,3,2
# tmts = [[[0, -1, 0, 0, 0],
#         [-1, -1, 0, 1, 1],
#         [0, 0, 0, 1, 1]],
#         [[0, -1, 0, 0, 0],
#         [-1, -1, 0, 1, 1],
#         [0, 0, 0, 1, 1]]]
        
future_tmts = copy.deepcopy(tmts)

def tomato(tmt,h,n,m):
    if h != 0 and tmt[h-1][n][m] != '-1':
        tmt[h-1][n][m] = '1'
    if n != 0 and tmt[h][n-1][m] != '-1':
        tmt[h][n-1][m] = '1'
    if m != 0 and tmt[h][n][m-1] != '-1':
        tmt[h][n][m-1] = '1'
    if h != H-1 and tmt[h+1][n][m] != '-1':
        tmt[h+1][n][m] = '1'
    if n != N-1 and tmt[h][n+1][m] != '-1':
        tmt[h][n+1][m] = '1'
    if m != M-1 and tmt[h][n][m+1] != '-1':
        tmt[h][n][m+1] = '1'

    return tmt
    
day = 0
not_t = False

while True:
    not_t = False
    for h in range(H):
        for n in range(N):
            if '1' in tmts[h][n]:
                for m in range(M):
                    if tmts[h][n][m] == '0':
                        not_t = True
                    if tmts[h][n][m] == '1':
                        future_tmts = tomato(future_tmts,h,n,m)

    if tmts == future_tmts:
        if not_t:
            day=-1
        break
    
    tmts = copy.deepcopy(future_tmts)
    day+=1

print(day)