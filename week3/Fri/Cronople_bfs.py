r,c,h = [int(i) for i in input().split()]

data = []
tomato = []
cnt = 0

def bfs(tmt):
    new_tomato = []
    # 6방향
    dx = (0, 0, 1, 0, 0, -1)
    dy = (0, 1, 0, 0, -1, 0)
    dz = (1, 0, 0, -1, 0, 0)
    
    #좌표 파악 후 0이면 1로 변경 후 새로운 리스트에
    # 좌표값 저장
    for i in tmt:
        for j in range(6):
            x = i[2] + dx[j]
            y = i[1] + dy[j]
            z = i[0] + dz[j]
            if -1 < x < r and -1 < y < c and -1 < z < h:
                if data[z][y][x] == 0:
                    data[z][y][x] = 1
                    new_tomato.append([z, y, x])
    return new_tomato


# 데이터 받기
for _ in range(h):
    temp = []
    for _ in range(c):
        temp.append([int(i) for i in input().split()])
    data.append(temp)

# 초기 데이터에서 익은 토마토 찾고 좌표값 저장
for i in range(h):
    for j in range(c):
        for k in range(r):
            if data[i][j][k] == 1:
                tomato.append([i, j, k])

# 좌표값 넣은 리스트로 bfs
while tomato:
    print(tomato)
    # 새로 익은 토마토가 없을 때까지 반복
    tomato = bfs(tomato)
    cnt += 1

# 안 익은 토마토가 있나 체크, 있다면 -1로 값 보내도록
for i in range(h):
    for j in range(c):
        for k in range(r):
            if data[i][j][k] == 0:
                cnt = 0

# while에서 토마토가 완전히 빌때까지 돌다보니 정답에서 +1로 나옴
print(cnt-1)