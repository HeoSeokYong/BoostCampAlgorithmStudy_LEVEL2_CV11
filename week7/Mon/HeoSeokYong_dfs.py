from itertools import product

def solution(numbers, target): # dfs
    answer = []
    def dfs(numbers, lev, res):
        if lev == len(numbers):
            answer.append(res)
        else:
            dfs(numbers, lev+1, res+numbers[lev])
            dfs(numbers, lev+1, res-numbers[lev])
        
    dfs(numbers, 0, 0)
    return answer.count(target)
    
def solution2(numbers, target): # product
    num_list = [(n, -n) for n in numbers]
    sum_list = list(map(sum, product(*num_list)))
    return sum_list.count(target)