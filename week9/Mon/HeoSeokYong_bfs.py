from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([(n,0)])
visited = [0]*100001
visited[n] = 1
while q:
    x, lev = q.popleft()
    if x == k:
        break
    if 2*x <= 100000 and not visited[2*x]:
        q.append((2*x, lev+1))
        visited[2*x] = 1
    if 0 <= x-1 < 100001 and not visited[x-1]:
        q.append((x-1, lev+1))
        visited[x-1] = 1
    if 0 < x+1 < 100001 and not visited[x+1]:
        q.append((x+1, lev+1))
        visited[x+1] = 1
        
print(lev)
