def solution(brown, yellow):
    area = brown + yellow
    
    for h in range(3, area//2): # 세로 길이
        if area % h == 0:
            w = area // h # 가로 길이
            br_num = (w * 2) + (h * 2) - 4
            if br_num == brown: 
                return [w, h]