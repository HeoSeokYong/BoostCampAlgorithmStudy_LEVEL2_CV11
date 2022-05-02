### 프로그래머스 Level3
### 이분탐색 | 입국심사
### https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
###
### original code:
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220406_prgkr_43238.py


def solution(n, times):
    '''이분 탐색 풀이
    
    참고 링크:
        - https://sohee-dev.tistory.com/123
        - https://velog.io/@ollabu3/프로그래머스-입국심사
    '''
    times = sorted(times)
    left, right = 1, times[-1] * n
    
    while left <= right:
        mid = (left + right) // 2
        counts = sum([ mid//t for t in times ])
        if counts < n: # 검사해야하는 수보다 적음
            left = mid + 1
        elif counts >= n: # 검사해야하는 수보다 많거나 같음
            answer = mid
            right = mid - 1
    
    return answer
