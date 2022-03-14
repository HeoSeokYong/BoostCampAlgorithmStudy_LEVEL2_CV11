def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)): # 2중 for문 앞에서 읽어나가고 뒤를 확인 
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
