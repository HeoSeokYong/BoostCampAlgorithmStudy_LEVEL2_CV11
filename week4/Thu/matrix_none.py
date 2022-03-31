import numpy as np
def solution1(arr1, arr2):
    bT = np.array(arr2)
    a = np.array(arr1)
    answer = ((a@bT).tolist())
    return answer

def solution(arr1, arr2):
    # (3,2) (2,2) ->(3,2)
    answer = [[0 for j in range(len(arr2[0]))] for i in range(len(arr1))]
    bT = np.transpose(arr2).tolist()    
    for i in range(len(arr1)): # 0 1 2
        for j in range(len(bT)):
            answer[i][j] = sum([a*b for a,b in zip(arr1[i], bT[j])])
    return answer
