### 백준
### 7569번 토마토
###
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220325_bj_7569.py

import sys
input = sys.stdin.readline

M, N, H = [ int(n) for n in input().split() ]
tomatos = [[[ int(n) for n in input().split() ] for _ in range(N) ] for _ in range(H) ]

ijks = list()
num_unripe = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 1:
                ijks.append((i, j, k))
            elif tomatos[i][j][k] == 0:
                num_unripe += 1

days_past = 0
while ijks:
    next_ijks = list()
    for i, j, k in ijks:
        for axis0, axis1, axis2 in (
            (1, 0, 0), (-1, 0, 0),
            (0, 1, 0), (0, -1, 0),
            (0, 0, 1), (0, 0, -1)
        ):
            result = False
            if 0 <= i+axis0 < H and 0 <= j+axis1 < N and 0 <= k+axis2 < M:
                if tomatos[i+axis0][j+axis1][k+axis2] == 0:
                    tomatos[i+axis0][j+axis1][k+axis2] = 1
                    num_unripe -= 1
                    result = True
            if result:
                next_ijks.append((i+axis0, j+axis1, k+axis2))
    days_past += 1 if next_ijks else 0
    ijks = next_ijks

answer = days_past if num_unripe == 0 else -1
print(answer)
