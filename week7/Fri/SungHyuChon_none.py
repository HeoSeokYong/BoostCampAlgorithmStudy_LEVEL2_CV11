# https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220422_prgkr_12979.py

def solution(n, stations, w):
    blank = list() # 빈 구간의 길이
    left = 1
    for s in stations:
        right = s - w
        blank.append(right-left)
        left = s + w + 1
    if left <= n:
        blank.append(n+1-left)
    
    # 각 빈 구간에 필요한 기지국 개수 계산
    answer = 0
    for b in blank:
        answer += b // (2*w + 1) + bool(b % (2*w + 1))

    return answer
