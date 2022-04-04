### 프로그래머스 Level2
### 정렬 | H-index
### https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
###
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220324_prgkr_42747.py

def solution(citations):
    citations = sorted(citations, reverse=True)
    
    answer = 0
    for i, c in enumerate(citations):
        h = i+1
        if h <= c:
            answer = h
        else:
            break
    
    return answer
