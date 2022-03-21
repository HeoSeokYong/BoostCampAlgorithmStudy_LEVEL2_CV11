k = int(input())
data = []
maxheight = 0
for i in range(k):
    tmp = [int(i) for i in input().split()]
    maxheight = max(maxheight, tmp[1])
    data.append(tmp)
'''
제일 긴 막대를 구하기 O
정렬 O
높은 기둥으로 양 쪽에서 접근하여 면적 구하기
or 
두개씩 검사, x+1보다 크면 이어서 만들기
오목한 부분이 있으면 좌우 중 작은 쪽에 맞추어 평탄화
or
max 값 기준으로 list
'''
data.sort()
answer = 0
max_x = [0, 0]
x = data[0][0]
y = data[0][1]

for i in data:
    if y < i[1]:
        answer += (i[0] - x) * y
        x = i[0]
        y = i[1]
    if maxheight == i[1]:
        max_x[0] = i[0]
        break

x = data[-1][0]
y = data[-1][1]
for i in data[::-1]:
    if y < i[1]:
        answer += (x - i[0]) * y
        x = i[0]
        y = i[1]
    if maxheight == i[1]:
        max_x[1] = i[0]
        break

answer += (max_x[1] + 1 - max_x[0]) * maxheight

print(answer)