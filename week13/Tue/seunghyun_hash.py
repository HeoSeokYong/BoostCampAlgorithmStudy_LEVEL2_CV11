def solution(clothes):
    answer = 0
    # cloth_list = [] # 문제에서 중복되는 옷은 없다고 했으니 체크 불필요
    cloth_dict = {}
    for c_name, c_type in clothes:
        # if c_name not in cloth_list:
            # cloth_list.append(c_name)
        if c_type in cloth_dict:
            cloth_dict[c_type]+=1
        else:
            cloth_dict[c_type]=1
    # print(cloth_dict)
    
    answer = 1
    for k, v in cloth_dict.items():
        answer *= (v+1)
    return answer-1