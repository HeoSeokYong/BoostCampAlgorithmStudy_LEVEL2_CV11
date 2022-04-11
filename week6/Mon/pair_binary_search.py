import sys
input = sys.stdin.readline

n, c = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))
 
data = sorted(data) 

# 인접한 두 공유기 사이의 최댓값 구하기

start = 1 # 최소 거리
end = (data[-1]-data[0]) // (c-1) # 최대 거리

answer = 0
while start <= end:
    mid = (start + end) // 2
    
    count = 1
    value = data[0]+mid

    for d in data[1:]:
        if d >= value: 
            value = d+mid
            count+=1
    
    if count >= c:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)
