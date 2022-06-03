def solution(n):
    answer = ''
    
    while n > 0:
        n, y = divmod(n-1, 3)
        answer += str(2 ** y)
    
    return answer[::-1]