def solution2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
                
    return answer

def solution(prices):
    p = len(prices)
    stack = [0]
    for i in range(1, p):
        answer = 0
        for j in range(p-i, p):
            answer += 1
            if prices[p-i-1] <= prices[j]:
                continue
            else:
                break
        stack.append(answer)
    stack.reverse()

    return stack