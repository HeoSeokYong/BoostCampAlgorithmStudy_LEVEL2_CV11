'''
해당 열은 못 쓰는 것
한 행당 한개
대각선

이중 포문
    행을 기준
        행보다 더 큰 숫자 위주 탐색
        
재귀함수
visited

첫 행의 n개의 위치로 도는 것으로 모든 경우를 탐색 가능
'''
n = int(input())
visited = []

def func(row, ans):
    if row == n:
        return ans + 1
    
    for col in range(n):
        flag = True
        for r, c in visited:
            if c == col or \
            abs(c - col) == abs(row - r):
                flag = False
                break
        if flag:
            visited.append((row, col))
            ans = func(row+1, ans)
            visited.pop()
    return ans
    
answer = func(0, 0)

print(answer)