def solution(number, k):
    answer = ''
    leng = len(number) - k
    # 9인 경우 예외처리(패싱) 예제 10번
    # 9가 굉장히 많은 경우

    while k > 0:
        max_num = max(number[:k+1])
        max_idx = number.index(max_num)
        k -= max_idx
        answer += number[max_idx]
        number = number[max_idx+1:]
        
        if len(answer) == leng:
            return answer

    return answer + number