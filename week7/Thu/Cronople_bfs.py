from collections import deque

def solution(arr):
    answer = [0, 0]
    deq = deque([arr])
    
    while deq:
        array = deq.popleft()
        flatten = sum(array, [])
        piv = flatten[0]
        isSame = True
        for i in range(1, len(flatten)):
            if piv != flatten[i]:
                val = len(array)//2
                deq.append([i[val:] for i in array[:val]])
                deq.append([i[val:] for i in array[val:]])
                deq.append([i[:val] for i in array[:val]])
                deq.append([i[:val] for i in array[val:]])
                isSame = False
                break
        if isSame:
            answer[piv] += 1
    
    return answer
