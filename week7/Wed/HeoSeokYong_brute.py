def solution(places):
    answer = []
    ls = [(1,1), (1,-1)]
    ls2 = [(2,0), (0,2)]
    
    for pla in places:
        flag = False
        # Room check
        for i in range(len(pla)): 
            for j in range(len(pla[0])):
                if pla[i][j] == 'P':
                    # 오른쪽, 아래
                    if (i < 4 and pla[i+1][j] == 'P') or (j < 4 and pla[i][j+1] == 'P'):
                            flag=True
                            break
                    # 대각선(우하, 좌하)
                    for a, b in ls:
                        if i<4 and (0 <= j+b < 5):
                            if pla[i+a][j+b] == 'P':
                                if pla[i+1][j] != 'X' or pla[i][j+b] != 'X':
                                    flag=True
                                    break
                    # 2칸 오른쪽, 아래
                    for a,b in ls2:
                        if i+a < 5 and j+b < 5:
                            if pla[i+a][j+b] == 'P':
                                if pla[i+(a//2)][j+(b//2)] != 'X':
                                    flag = True
                                    break
            if flag:
                break
        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer