def solution(phone_book):
    
    phone_book = sorted(phone_book)
    print(phone_book)
    for i in range(len(phone_book)-1):
        now = phone_book[i]
        if now == phone_book[i+1][:len(now)]:
            return False
    
    return True
