import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

dp = [[0 for i in range(sum(cost)+1)] for j in range(N+1)] 

for i in range(1, N+1):
    for j in range(1, sum(cost)+1):
        if j >= cost[i]:
            dp[i][j] = max(dp[i-1][j-cost[i]] + mem[i], dp[i-1][j])

bf=False
for i in range(sum(cost)+1):
    for j in range(1, N+1):
        if dp[j][i] >= M:
            print(i)
            bf=True
            break
    if bf:
        break
