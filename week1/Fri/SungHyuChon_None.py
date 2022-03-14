### 백준
### 1074번 Z
###
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220311_bj_1074.py

N, r, c = [ int(n) for n in input().split() ]
answer = 0

n = N
while n > 0:
    if r >= 2 ** (n-1):
        answer += 2 ** (2*n-1)
        r -= 2 ** (n-1)
    n -= 1

n = N
while n > 0:
    if c >= 2 ** (n-1):
        answer += 2 ** (2*n-2)
        c -= 2 ** (n-1)
    n -= 1

print(answer)
