import sys
input = sys.stdin.readline

def check4way(data, visited, i, j):
    """
    만약 끝이거나, X, O가 있으면 바로 정지
    .을 만나면 해당 . 위치는 visited = True
    그래서 False인 친구들만 B로 변환
    """
    for r in range(i+1, len(data)):
        if data[j][r] == '.':
            visited[j][r] = True
        else:
            break
    for l in range(i-1, -1, -1):
        if data[j][l] == '.':
            visited[j][l] = True
        else:
            break
    for u in range(j-1, -1, -1):
        if data[u][i] == '.':
            visited[u][i] = True
        else:
            break
    for d in range(j+1, len(data)):
        if data[d][i] == '.':
            visited[d][i] = True
        else:
            break

n = int(input())
data = []
visited = []
Oqueue = []
for i in range(n):
    tmp = input()
    tmp_list = []
    tmp_visit = []
    for j in range(n):
        tmp_list.append(tmp[j])
        if tmp[j] != '.':
            if tmp[j] == 'O':
                Oqueue.append([j, i])
            tmp_visit.append(True)
        else:
            tmp_visit.append(False)
    visited.append(tmp_visit)
    data.append(tmp_list)

############################
for i, j in Oqueue:
    check4way(data, visited, i, j)

for i in range(n):
    for j in range(n):
        if visited[j][i] == False:
            data[j][i] = 'B'


answer = ''
for i in data:    
    answer += ''.join(i) + '\n'
    
print(answer.rstrip())