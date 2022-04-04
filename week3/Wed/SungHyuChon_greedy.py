### 프로그래머스 Level2
### 탐욕법(Greedy) | 큰 수 만들기
### https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
###
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220323_prgkr_42883.py

def solution(number, k):
    # 맨 왼쪽부터 i+1번째 숫자보다 작은 i번째 숫자를 찾아서 제거, 제거 후 i-1번째부터 재시작
    # (i-1번째 숫자까지는 모두 역순으로 정렬되어 있으므로 돌아갈 필요 X)

    idx = 0
    while k != 0:
        for i in range(idx, len(number)):
            curr_num = int(number[i])
            next_num = int(number[i+1]) if i+1 < len(number) else 10 # 마지막 숫자까지 도달했다면 해당 숫자 무조건 제거
            if curr_num < next_num:
                num_left = number[:i]
                num_right = number[i+1:] if i+1 < len(number) else ''
                number = num_left + num_right
                break
        k -= 1
        idx = max(0, i-1)

    return number
