def solution(name):
    alp = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    comp = [100 if n == 'A' else 0 for n in name]
    answer = []
    comp[0] = 100
    def dfs(comp, res, cursor):
        if sum(comp) == 100 * len(comp):  
            answer.append(res)
        for i in range(len(comp)):
            if comp[i] != 100:
                dist = abs(i - cursor)
                if dist >= len(name) // 2:
                    dist = len(name) - dist
                dist_alp = alp.index(name[i])
                if dist_alp >= len(alp) // 2:
                    dist_alp = len(alp) - dist_alp
                comp[i] = 100
                dfs(comp, res + dist + dist_alp, i)
                comp[i] = 0
                
    dfs(comp, alp.index(name[0]), 0)

    return min(answer)

def solution_greedy(name):
    alp = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    comp = [100 if n == 'A' else 0 for n in name]

    answer = alp.index(name[0])
    comp[0] = 100
    cursor = 0
    
    while True:
        for i in range(1, len(comp)):
            if comp[i] != 100:
                dist = abs(i - cursor)
                if dist >= len(name) // 2:
                    dist = len(name) - dist
                dist_alp = alp.index(name[i])
                if dist_alp >= len(alp) // 2:
                    dist_alp = len(alp) - dist_alp
                comp[i] = dist + dist_alp

        cursor = comp.index(min(comp))
        answer += comp[cursor]
        comp[cursor] = 100
        if sum(comp) == 100 * len(comp):
            break

    return answer