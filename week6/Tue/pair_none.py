### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220412_prgkr_12938.py

def solution(n, s):
    if s < n:
        return [-1]
    
    mok = s // n
    answer = [ mok ] * n
    
    namoji = s % n
    for i in range(len(answer)-1, len(answer)-1-namoji, -1):
        answer[i] += 1
    
    return answer
