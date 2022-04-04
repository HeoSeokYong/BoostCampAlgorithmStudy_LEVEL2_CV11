### 프로그래머스 Level3
### 연습문제 | 2 x n 타일
### https://programmers.co.kr/learn/courses/30/lessons/12900?language=python3

# from math import comb

def solution(n):
#     # 1. 조합 (시간 초과)
#     answer = 0
    
#     r = 0
#     while n >= 0:
#         answer += comb(n+r, r) # 중복 조합
#         n -= 2
#         r += 1
    
#     return answer % 1000000007
    
    # 2. 피보나치
    fibo = [0] * (n+1)
    
    fibo[1], fibo[2] = 1, 2
    for f_idx in range(3, len(fibo)):
        fibo[f_idx] = (fibo[f_idx-1] % 1000000007) + (fibo[f_idx-2] % 1000000007)
    
    return fibo[-1] % 1000000007
