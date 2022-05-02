# https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220421_prgkr_68936.py

import numpy as np
from collections import deque

def solution(arr):
    arr = np.array(arr)
    arrs = deque([arr])
    zeros, ones = 0, 0
    
    while arrs:
        a = arrs.popleft()
        if 0 not in a:
            ones += 1
        elif 1 not in a:
            zeros += 1
        elif len(arr) > 1:
            arrs.append(a[:len(a)//2, :len(a)//2])
            arrs.append(a[:len(a)//2, len(a)//2:])
            arrs.append(a[len(a)//2:, :len(a)//2])
            arrs.append(a[len(a)//2:, len(a)//2:])
    
    return [zeros, ones]
