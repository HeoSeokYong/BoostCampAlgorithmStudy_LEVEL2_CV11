import math
def solution(brown, yellow):
    answer = []
    # 테두리 한줄: brown
    # x >= y
    # yellow 만들 수 있는 모든 경우의 수
    
    total_area = brown+yellow # 전체 카펫 크기
    for i in range(yellow+1, 0, -1):
        if yellow%i==0: # yellow의 약수일 때 
            x, y = i, yellow//i 
            if total_area - (x+2)*(y+2) == 0:
                answer = [x+2, y+2]
                break

    return answer