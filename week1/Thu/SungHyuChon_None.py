### 프로그래머스 Level2
### 주식가격 | 스택/큐
### https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
###
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220310_prgkr_42584.py

def solution(prices):
    answer = list(range(len(prices)-1, -1, -1))
    
    price_stack, idx_stack = [0], [-1]
    for i, p in enumerate(prices):
        while idx_stack[-1] != -1 and p < price_stack[-1]:
            price_stack.pop()
            temp_i = idx_stack.pop()
            answer[temp_i] = i - temp_i
        
        price_stack.append(p)
        idx_stack.append(i)
                
    return answer