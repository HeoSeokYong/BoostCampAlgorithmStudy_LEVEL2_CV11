import sys 
input = sys.stdin.readline
n = int(input())
arr = input().split()

"""
backtracking
9부터 넣어보고 9보다 큰게 없으니까 돌아가서 8로 시작하고 
그다음 8을 넣고 9를 넣었을 때 만족하니까 계속 이어짐 
"""
answer = ['','']
def dfs_max(n, str_max, visited):
    if n + 1 == len(str_max) : # 3 == 3
        answer[0] = (str_max)
        return 
    if answer[0] == '' : 
        for i in range(9, 8-n, -1): # [9,8,7] visited 
            if visited[i] == 0:
                visited[i] = 1
                str_max += str(i)
                if len(str_max) >= 2:
                    if arr[len(str_max)-2] == '>' and str_max[-2] > str_max[-1]:
                        dfs_max(n, str_max, visited)
                    if arr[len(str_max)-2] == '<' and str_max[-2] < str_max[-1]:
                        dfs_max(n, str_max, visited)
                else : 
                    dfs_max(n, str_max, visited)
                str_max = str_max[:-1]
                visited[i] = 0

def dfs_min(n, str_max, visited):
    if n + 1 == len(str_max) : # 3 == 3
        answer[1] = (str_max)
        return 
    if answer[1] == '' : 
        for i in range(0, n+1): # [0,1,2] visited 
            if visited[i] == 0:
                visited[i] = 1
                str_max += str(i)
                if len(str_max) >= 2:
                    if arr[len(str_max)-2] == '>' and str_max[-2] > str_max[-1]:
                        dfs_min(n, str_max, visited)
                    if arr[len(str_max)-2] == '<' and str_max[-2] < str_max[-1]:
                        dfs_min(n, str_max, visited)
                else : 
                    dfs_min(n, str_max, visited)
                str_max = str_max[:-1]
                visited[i] = 0
dfs_max(n, '', [0]*10)
dfs_min(n, '', [0]*10)
print(answer[0] + '\n'+answer[1])
