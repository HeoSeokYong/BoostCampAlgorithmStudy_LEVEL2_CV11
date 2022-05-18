# https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220516_prgkr_42842.py

def solution(brown, yellow):
    # (w-1) + (h-1) == brown // 2
    # (w-2) * (h-2) == yellow
    
    h, w = 1, yellow
    while h <= w:
        if yellow % h:
            h += 1; continue
        w = yellow // h
        if (w+1) + (h+1) == brown // 2:
            return [w+2, h+2]
        h += 1
