# https://programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    binn = bin(n)[2:]
    lenn = (binn.count('1'))
    for i in range(n+1, 1000001):
        if bin(i)[2:].count('1') == lenn:
            return (i)
    return 0
