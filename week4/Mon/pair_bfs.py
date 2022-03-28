from collections import deque
import sys
input = sys.stdin.readline #####

n, m, k, x = map(int, input().split())

graph = {k:[] for k in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])
distance = {k:-1 for k in range(1, n+1)}
distance = [-1]*(n+1)
distance[x] = 0 

while queue:
    now = queue.popleft()
    
    if distance[now]+1 > k:
        break
    
    for dest in graph[now]:
        if distance[dest] == -1: 
            distance[dest] = distance[now] + 1 # 거리 업데이트
            queue.append(dest)

string = ''
for i in range(len(distance)):
    if distance[i]==k:
        string += str(i) + '\n' 

if len(string)==0:
    print(-1)
else:
    print(string)