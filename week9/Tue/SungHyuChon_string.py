# https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220503_prgkr_12911.py

def solution(n):
    one_count = bin(n).count('1')
    n += 1
    while bin(n).count('1') != one_count:
        n += 1
    return n
