### 프로그래머스 Level2
### 연습문제 | 땅따먹기
### https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3
###
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220322_prgkr_12913.py

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            max_prev = max(land[i-1][:j] + land[i-1][j+1:])
            land[i][j] = land[i][j] + max_prev
    
    return max(land[-1])
