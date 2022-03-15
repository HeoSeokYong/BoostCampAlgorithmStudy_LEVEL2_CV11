### 프로그래머스 Level3
### 동적계획법(Dynamic Programming) | 정수 삼각형
### https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    height = len(triangle)
    
    for i in range(1, height):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    
    answer = max(triangle[-1])
    
    return answer
