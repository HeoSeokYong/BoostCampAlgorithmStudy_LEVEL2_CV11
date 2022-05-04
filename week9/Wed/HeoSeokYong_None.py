def solution(record):
    answer = []
    records = []
    naming = {}
    
    for r in record:
        records.append(r.split(' '))
        
    # 이름 최신화
    for rec in records:
        if rec[0] != 'Leave':
            naming[rec[1]] = rec[2]
    
    for rec in records:
        if rec[0] == 'Enter':
            answer.append(naming[rec[1]] + '님이 들어왔습니다.')
        elif rec[0] == 'Leave':
            answer.append(naming[rec[1]] + '님이 나갔습니다.')
            
    return answer