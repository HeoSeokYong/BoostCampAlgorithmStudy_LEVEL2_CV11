maxx = 0

def dfs(st, dungeons, curr_k, visited):
	global maxx
	ed_lev = len(dungeons)
	for i in range(ed_lev): # 0 1 2 
		if visited[i] == 0 and curr_k >= dungeons[i][0]:
			visited[i] = 1
			maxx = max(st+1, maxx)
			dfs(st + 1, dungeons, curr_k - dungeons[i][1], visited)
			visited[i] = 0

def solution(k, dungeons):
	visited = [0] * len(dungeons)

	dfs(0, dungeons, k, visited)
	return maxx
