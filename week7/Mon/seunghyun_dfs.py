# dfs(+)
# dfs(-)
def solution(numbers, target):
    global answer
    answer = 0
    dfs(index=-1, now=0, array=numbers, target=target)
    return answer

def dfs(index, now, array, target):
    global answer
    
    if index+1 >= len(array):
        if now == target: # target값과 동일한 경우
            answer += 1
    else:
        dfs(index+1, now+array[index+1], array, target)
        dfs(index+1, now-array[index+1], array, target)