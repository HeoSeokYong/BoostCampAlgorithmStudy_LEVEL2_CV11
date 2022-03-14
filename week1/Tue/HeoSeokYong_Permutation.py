from itertools import permutations

def explore(k, dungeons):
    cnt = 0
    for d in dungeons:
        if k >= d[0]:
            k -= d[1]
            cnt+=1
            
    return cnt

def solution(k, dungeons):
    answer = 0
    perm = permutations(dungeons, len(dungeons))

    for p in perm:
        tmp = explore(k, p)
        if tmp > answer:
            answer = tmp
            
    return answer