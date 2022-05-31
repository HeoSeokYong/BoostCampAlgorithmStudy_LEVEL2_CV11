def solution(clothes):
    answer = 1
    clo = {c[1]: [] for c in clothes}
        
    for cl in clothes:
        clo[cl[1]].append(cl[0])
    
    
    for k in clo.keys():
        answer *= (len(clo[k])+1)
        
    return answer - 1