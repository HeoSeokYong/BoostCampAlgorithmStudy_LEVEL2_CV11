def solution(prices)
    answer=[]
    for i, v in enumerate(prices)
        cnt = 0
        for k in range(i, len(prices)-1)
            if v  prices[k]
                break
            else
                cnt += 1
        answer.append(cnt)
    return answer