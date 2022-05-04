
#  https://programmers.co.kr/learn/courses/30/lessons/42888

def solution1(record):
    users = {}
    for i in range(len(record)):
        record[i] = record[i].split()
        if record[i][0] == 'Enter' or record[i][0] == 'Change':
            users[record[i][1]] = record[i][2]
    # print(users)
    finalstr = []
    for item in record:
        if item[0] == 'Enter':
            finalstr.append("{}님이 들어왔습니다.".format(users[item[1]]))
        if item[0] == 'Leave':
            finalstr.append("{}님이 나갔습니다.".format(users[item[1]]))
    return(finalstr)
