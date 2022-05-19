# 같은 구성: 문자+개수
# 비슷한 구성 : 한 문자(+, -, 교체)로 구성이 같아지는 경우
from copy import deepcopy

N = int(input())
t_word = input()
target = {}
for w in t_word:
    if w in target:
        target[w]+=1
    else:
        target[w]=1

# 비슷한 구성이 될 수 있는 경우
# => 단어 개수의 차이가 1 이하인 경우
answer = 0
for _ in range(N-1):
    word = input()
    diff =  abs(len(word)-len(t_word))
    if diff>1: # 차이가 2 이상이면 다른 단어
        continue
    
    elif diff==1: # 차이가  1(+,-) 일때
        target_ = deepcopy(target)
        diff_counter = 0
        for w in word:
            if w in target_ and target_[w]>0:
                target_[w] -=1
            else:
                diff_counter+=1
        if sum(target_.values())<=1 and diff_counter<=1:
            answer+=1

    elif diff==0: # 0(교체)
        target_ = deepcopy(target)
        for w in word:
            if w in target_ and target_[w]>0:
                target_[w] -=1
        if sum(target_.values())<=1:
            answer+=1

print(answer)
