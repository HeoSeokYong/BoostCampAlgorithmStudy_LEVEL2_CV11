import numpy as np

def solution(rows, columns, queries):
    answer = []
    mat = np.empty((0,columns), int)
    
    # make matrix
    cnt = 1
    for r in range(rows):
        tmp = []
        for c in range(columns):
            tmp.append(cnt)
            cnt+=1
        mat = np.append(mat, np.array([tmp]),axis=0)

    for q in queries:
        x1, y1, x2, y2 = [x-1 for x in q]
        topleft = mat[x1+1][y1]
        botright = mat[x2-1][y2]
        topright = mat[x1][y2-1]
        botleft = mat[x2][y1+1]

        left = np.append(mat[x1+1:x2+1,y1], np.array([botleft]))
        right = np.append(np.array([topright]), mat[x1:x2,y2])
        top = np.append(np.array([topleft]), mat[x1][y1:y2])
        bot = np.append(mat[x2][y1+1:y2+1], np.array([botright]))
        
        mat[x1:x2+1,y1] = left
        mat[x1:x2+1,y2] = right
        mat[x1][y1:y2+1] = top
        mat[x2][y1:y2+1] = bot
        
        answer.append(int(np.min(np.concatenate((left,right,top,bot)))))

    return answer