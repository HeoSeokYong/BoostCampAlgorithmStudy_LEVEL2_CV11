### 프로그래머스 Level2
### 피로도 | 위클리 챌린지
### https://programmers.co.kr/learn/courses/30/lessons/87946?language=python3
###
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220308_prgkr_87946.py

def search(k, dungeons, visited, n_dungeon: int=0):
    if sum(visited) == len(visited):
        return n_dungeon
    
    best_depth = n_dungeon
    for i, d in enumerate(dungeons):
        if k >= d[0] and visited[i] != 1:
            visited[i] = 1
            explored_depth = search(
                k-d[1],
                dungeons,
                visited,
                n_dungeon+1
            )
            if explored_depth > best_depth:
                best_depth = explored_depth
            visited[i] = 0
    
    return best_depth

def solution(k, dungeons):
    visited = [ 0 for _ in dungeons ]
    answer = search(k, dungeons, visited)
    return answer
