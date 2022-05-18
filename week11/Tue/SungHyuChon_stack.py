# https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220517_prgkr_12973.py

def solution(s):
    stack = ['_']
    for c in s:
        if c != stack[-1]:
            stack.append(c)
        else:
            stack.pop()
    return int(len(stack) == 1)
