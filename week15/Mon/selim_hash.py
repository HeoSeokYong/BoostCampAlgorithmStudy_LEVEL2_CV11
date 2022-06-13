def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    # print(phone_book)
    numDict = {phone_book[0]:1}
    maxlen = len(phone_book[0])
    # print(numDict)
    for item in phone_book:
        for i in range(1, len(item)):
            if i <= maxlen : 
                if item[:i] in numDict : 
                    return False 
        numDict[item] = 1
        maxlen = max(len(item), maxlen)
        # print(numDict)
    return True
