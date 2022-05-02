### 프로그래머스 Level2
### 찾아라 프로그래밍 마에스터 | 게임 맵 최단거리
### https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3
###
### original code:
### https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220405_prgkr_1844.py

from collections import deque

def solution(maps):
    prev_xy, curr_xy = deque(), deque()

    steps = 1
    found = False
    prev_xy.append((0, 0))
    maps[0][0] = 0
    while prev_xy:
        x, y = prev_xy.popleft()
        for axis0, axis1 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x+axis0 < len(maps) and 0 <= y+axis1 < len(maps[0]):
                if x+axis0 == len(maps)-1 and y+axis1 == len(maps[0])-1:
                    found = True
                    steps += 1
                    break
                elif maps[x+axis0][y+axis1] == 1:
                    maps[x+axis0][y+axis1] = 0
                    curr_xy.append((x+axis0, y+axis1))
        if found:
            break
        if len(prev_xy) == 0:
            prev_xy, curr_xy = curr_xy, deque()
            steps += 1
    
    return steps if found else -1
