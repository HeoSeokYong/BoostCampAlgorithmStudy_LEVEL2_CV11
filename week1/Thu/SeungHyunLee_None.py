def solution(prices):
    
    # 가격이 떨어지지 않는 기간에 대한 list의 모든 값 0으로 초기화
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                # 가격이 떨어지면 1초간 가격이 떨어지지 않은 것으로 간주하므로 +1
                answer[i]+=1
                break
    return answer