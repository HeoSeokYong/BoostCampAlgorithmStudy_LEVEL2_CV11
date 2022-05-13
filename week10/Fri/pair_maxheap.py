import heapq

def solution(n, works):
    
    works = [-i for i in works]
    heapq.heapify(works)
    for _ in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1)
    
    return sum([i**2 for i in works if i < 0])

    # 트라이 1, 포인터를 통한 계산
    # works.sort(reverse=True)
    # cur = 0 
    # while n > 0:
    #     works[cur] -= 1
    #     n -= 1
    #     if cur == len(works) - 1:
    #         cur = 0
    #     elif works[cur] < works[cur+1]:
    #         cur += 1
    
    # 트라이 2, 평균을 통한 계산
    # summ = sum(works)
    # lenn = len(works)
    # while n > 0:
    #     avg = summ / lenn
    #     for i in range(len(works)):
    #         if works[i] >= avg and n > 0:
    #             print(avg)
    #             n-= 1
    #             summ -= 1
    #             works[i] -= 1
    #         else:
    #             break
    