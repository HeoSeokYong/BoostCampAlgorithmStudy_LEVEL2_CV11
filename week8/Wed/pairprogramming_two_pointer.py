import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
answer = 0
'''
a, b 포인트
전체 길이의 합에 절반이 bast **
부분집합으로 best와 근사하는 값 찾기
'''
sumd = sum(data)
best = sum(data) / 2
s, e = 0, 1
stack = data[0]

while e <= len(data):
    if stack <= best:
        e += 1
        if e > len(data):
            break
        stack += data[e-1]
    else:
        answer = max(min(stack, sumd-stack), answer)
        stack -= data[e-1]
        answer = max(min(stack, sumd-stack), answer)
        s += 1
        stack += data[e-1] - data[s-1]
        #answer = max(min(stack, sumd-stack), answer)
        
print(answer)