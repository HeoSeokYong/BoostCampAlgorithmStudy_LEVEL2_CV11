'''
길찾기 문제처럼 접근?(queue 사용)
알파벳 하나 달라지는 것만 q에 넣기.
ex. 
1. hit -> hot
2. hot -> dot, lot
3. dot -> dog / lot -> log
4. dog -> cog / log -> cog [answer=4]
'''

from collections import deque

def check_word(w1, w2):
    counter=0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            counter+=1
        if counter>1:
            break
    return counter==1

def bfs(q, words):
    temp_q = deque()
    for now in q:
        if now in words:
            words.remove(now)

        for w in words:
            if check_word(now, w):                
                temp_q.append(w)
    return temp_q, words

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    q = deque([begin])
    words = [begin] + words
    while q:
        q, words = bfs(q, words)
        answer+=1
        if target in q:
            return answer

    return 0