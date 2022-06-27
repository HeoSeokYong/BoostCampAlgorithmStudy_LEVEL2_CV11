from collections import deque

def solution(number, k):
    que = deque()
    le = len(number) - k
    
    for i in range(len(number)):
        if que:
            while que and que[-1] < number[i] and k != 0:
                que.pop()
                k -= 1
        que.append(number[i])
        if k == 0:
            break
    
    answer = ''.join(list(que)) + number[i+1:]
    return answer[:le]
    
    
    
# def solution(number, k):
#     answer = ''
#     leng = len(number) - k
#     # 9인 경우 예외처리(패싱) 필요 예제 10번 시간초과
#     # 9가 굉장히 많은 경우

#     while k > 0:
#         max_num = max(number[:k+1])
#         max_idx = number.index(max_num)
#         k -= max_idx
#         answer += number[max_idx]
#         number = number[max_idx+1:]
        
#         if len(answer) == leng:
#             return answer

#     return answer + number