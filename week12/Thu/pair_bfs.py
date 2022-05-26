# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque 

def solution(n, computers):
    answer = 0
    visited = [0] * n 
    for i in range(n):
        if visited[i] == 0:
            # print(i)
            que = deque()
            que.append(i)
            while que : 
                now = que.popleft() 
                visited[now] = 1
                for j in range(n):
                    if computers[now][j] == 1 and visited[j] == 0: 
                        que.append(j)      
            answer += 1
    return answer
# stack - dfs 
