from collections import deque

def solution(arr):
    answer = []
    zero, one = 0, 0
    arr_deq = deque()
    arr_deq.append(arr)
    
    while arr_deq:
        tmp = arr_deq.popleft()
        t = sum(tmp, []) # 이거 신기합니다!
        if 0 not in t:
            one += 1
        elif 1 not in t:
            zero += 1
        else:
            arr_deq.append([i[len(tmp)//2:] for i in tmp[len(tmp)//2:]])
            arr_deq.append([i[:len(tmp)//2] for i in tmp[len(tmp)//2:]])
            arr_deq.append([i[len(tmp)//2:] for i in tmp[:len(tmp)//2]])
            arr_deq.append([i[:len(tmp)//2] for i in tmp[:len(tmp)//2]])
    
    return [zero, one]