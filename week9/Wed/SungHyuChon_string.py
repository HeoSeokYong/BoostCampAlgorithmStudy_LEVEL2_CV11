# https://github.com/shhommychon/CodingSkillTest/blob/master/Python/Naver_boostcamp/220504_prgkr_42888.py

def solution(record):
    user_dict = dict()
    record_uid = []
    for r in record:
        if r[:5] == "Enter":
            type_, uid, uname = r.split(' ')
            record_uid.append((uid, "님이 들어왔습니다."))
            user_dict[uid] = uname
        elif r[:5] == "Leave":
            type_, uid = r.split(' ')
            record_uid.append((uid, "님이 나갔습니다."))
        else: # if r[:5] == "Chang":
            type_, uid, uname = r.split(' ')
            user_dict[uid] = uname
    
    answer = []
    for r in record_uid:
        uid, log = r
        answer.append(user_dict[uid]+log)
    
    return answer