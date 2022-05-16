def solution(brown, yellow):
    summ = brown + yellow 
    x, y = summ / 2, 2 
    maxx = summ ** 0.5
    while y <= maxx :
        if x == int(x) and y == int(y):
            # print(x, y)
            if yellow == (y-2)*(x-2):
                break
                # print('answer', x,y)
        y += 1
        x = summ / y
    return [x, y]
