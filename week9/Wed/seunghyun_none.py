def solution(record):
    answer = []
    new_records = {}
    for rc in record:
        temp_str = rc.split(" ")
        status, id_ = temp_str[0], temp_str[1:]
        if status == "Enter":
            new_records[id_[0]] = id_[1]
            answer.append(f"{id_[0]}님이 들어왔습니다.")
        elif status == "Change":
            new_records[id_[0]] = id_[1]
        else:
            answer.append(f"{id_[0]}님이 나갔습니다.")

    result = []
    for i in answer:
        id__ = i.split("님이")[0]
        result.append(i.replace(id__, new_records[id__]))

    return result