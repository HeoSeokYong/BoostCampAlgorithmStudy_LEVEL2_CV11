def solution(genres, plays):
    answer = []
    dict = {}
    
    for i in range(len(genres)):
        if genres[i] in dict.keys():
            dict[genres[i]][0] += plays[i]
            dict[genres[i]].append([plays[i], i])
        else:
            dict[genres[i]] = [plays[i], [plays[i], i]]
    
    lst =  []
    for k in dict.keys():
        dict[k][1:] = sorted(dict[k][1:], key = lambda x:x[0]*(-1))
    
    lst = list(dict.values())
    lst.sort(reverse=True)
    
    for l in lst:
        for i in range(1, min(3, len(l))):
            answer.append(l[i][1])
    
    return answer