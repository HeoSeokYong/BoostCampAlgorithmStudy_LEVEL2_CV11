# https://programmers.co.kr/learn/courses/30/lessons/42883#
from collections import deque 

def solution(number, k):
    removed = 0
    que = deque()
    for i in range(len(number)):
        if len(que) == 0:
            que.append(number[i]) # 1 
        elif que:
            while que and number[i] > que[-1] and removed != k: 
                que.pop()
                removed += 1
            que.append(number[i])
        if removed == k:
            break
    print(list(que))
    for j in range(i+1, len(number)):
        que.append(number[j])
    a = ''.join(list(que))
    return a[:len(number)-k]


# 시간초과 
# from itertools import combinations 
# def solution(number, k):
#     newlst = []
#     for item in (combinations(number, len(number)-k)): 
#         newint = ''.join(item)
#         newlst.append(int(newint))
#     print(newlst)
#     return str(max(newlst))
