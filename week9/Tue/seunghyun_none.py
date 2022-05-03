import sys     
sys.setrecursionlimit(10000) # 재귀 사용으로 인한 문제였음

def solution(n):
    # n = 78
    answer = n+1
    n_count = one_counter(n, 0)
    while True:
        if one_counter(answer, 0) == n_count:
            break
        answer+=1
    return answer

# 이진수 변환하며 1 개수 세기
def one_counter(n, counter):
    mok, remain = n // 2, n%2
    if remain == 1:
        counter+=1
    if mok== 0 :
        return counter
    else :
        return one_counter(mok, counter)