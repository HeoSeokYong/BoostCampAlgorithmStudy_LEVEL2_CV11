def solution(clothes):
    closet = {}
    for item in clothes : 
        if item[1] not in closet: 
            closet[item[1]] = 1
        else : 
            closet[item[1]] += 1
    # print(closet)
    answer = 1
    for key in closet : 
        answer *= (closet[key] + 1)
    return answer -1
