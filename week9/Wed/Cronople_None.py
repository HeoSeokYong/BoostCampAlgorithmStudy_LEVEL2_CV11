def solution(record):
    answer = []
    name = {}
    log = []
    
    for i in record:
        info = i.split()
        if info[0] != 'Leave':
            name[info[1]] = info[2]
            if info[0] == 'Enter':
                log.append([info[1], '님이 들어왔습니다.'])
        else:
            log.append([info[1], '님이 나갔습니다.'])
    
    for i in log:
        answer.append(name[i[0]] + i[1])
    
    return answer