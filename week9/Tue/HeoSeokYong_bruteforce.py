def solution(n):
    answer = n
    binn = bin(n)[2:].count('1')
    
    while True:
        answer = answer + 1
        big_binn = bin(answer)[2:].count('1')
        if binn == big_binn:
            break
    
    return answer