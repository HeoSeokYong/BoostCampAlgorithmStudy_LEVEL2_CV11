'''
참고: https://pacific-ocean.tistory.com/159
'''

N = int(input())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = sorted(data, key=lambda x: x[0]) # A에 대해서 정렬
dp = [0 for i in range(N)]
b = [i[1] for i in data] # b에 대해 최장 증가 부분 수열 구하기.

for i in range(N):
    for j in range(i):
        if b[i]>b[j] and dp[i]<dp[j]:
            # print(b[i], b[j], dp[i], dp[j])
            dp[i] = dp[j]
    dp[i]+=1 # 최소 1.
    # print(dp)
    # print()
print(N-max(dp)) # 전체 전기줄 개수 - LIS

