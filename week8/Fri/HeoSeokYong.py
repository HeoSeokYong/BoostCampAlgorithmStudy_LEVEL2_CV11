def solution(s):
    answer = []
    
    s = s[2:-2]
    tp = s.split('},{')
    tp = [t.split(',') for t in tp]
    tp.sort(key=lambda x: len(x))
    
    for t in tp:
        for i in t:
            if int(i) not in answer:
                answer.append(int(i))
                break
    
    return answer