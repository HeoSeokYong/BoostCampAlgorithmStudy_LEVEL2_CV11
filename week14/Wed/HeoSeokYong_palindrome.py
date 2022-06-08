def solution(s):
    answer = 1

    for i in range(len(s)-1):
        idx = 1
        while (i-idx) >= 0 and (i+idx) < len(s):
            if s[i-idx] != s[i+idx]: 
                break
            idx+=1
        answer = max(answer, 1 + 2*(idx-1))
        
        if s[i] == s[i+1]:
            idx = 1
            while (i-idx) >= 0 and (i+1+idx) < len(s):     
                if s[i-idx] != s[i+1+idx]: 
                    break
                idx+=1
            answer = max(answer, 2*idx)

    return answer