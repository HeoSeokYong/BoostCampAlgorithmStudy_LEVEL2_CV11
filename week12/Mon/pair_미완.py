answer = []
def solution(tickets):
    global answer
    trip_dict = {}
    visited_dict = {}
    for t in tickets:
        if t[0] in trip_dict:
            trip_dict[t[0]].append(t[1])
            visited_dict[t[0]].append(0)
        else:
            trip_dict[t[0]] = [t[1]]
            visited_dict[t[0]] = [0]
    for t in trip_dict:
        trip_dict[t] = sorted(trip_dict[t])
    
    # dfs
    len_ = len(tickets)
    print(trip_dict)
    answer.append("ICN")
    dfs("ICN", trip_dict, visited_dict, len_)
    return answer

def dfs(now, trip_dict, visited_dict, len_):
    global answer
    if len(answer)==len_+1:
        return
    else:
        if now in trip_dict:
            for t in trip_dict[now]:
                idx = trip_dict[now].index(t)
                if visited_dict[now][idx]==0:
                    visited_dict[now][idx]=1
                    answer.append(t)
                    dfs(t, trip_dict, visited_dict, len_)
                    if len(answer)==len_+1:
                        return
                    visited_dict[now][idx]=0
                    answer.pop()