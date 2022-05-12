import sys
from collections import deque
input = sys.stdin.readline 

n = int(input())
m = int(input())
connected = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)
visited = [0] * (n+1)
visited[1] = 1
visited[0] = -1
que = deque(connected[1])
while que:
    cur = que.popleft()
    if not visited[cur]:
        visited[cur] = 1 
        for item in connected[cur]:
            if not visited[item]:
                que.append(item)
print(sum(visited))
    
