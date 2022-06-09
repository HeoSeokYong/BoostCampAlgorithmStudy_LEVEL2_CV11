import sys 
input = sys.stdin.readline
n, x = map(int, input().split())
sys.setrecursionlimit(10**9)

# class FibDict(dict):
#     def __init__(self):
#         self[0] = 'P'
#     def __missing__(self, k):
#         fibk = self[k] = 'B' + self[k-1] + 'P' + self[k-1] + 'B'
#         return fibk

# def bur(lev): 
#     if lev == 0: return 'P'
#     else : 
#         lev1 = bur(lev-1)
#         return 'B' + lev1 + 'P' + lev1 + 'B'
# answer = bur(n)[:x].count('P')

# fibd = FibDict()
# answer = fibd[n]
# answer = answer[:x].count('P')

# b = 'P'
# lenn = 1 
# for i in range(1, n+1): #0~49
#     if lenn > x: 
#         b = 'B' + b + 'P'
#     else : # lenn <= x 
#         b = 'B' + b + 'P' + b + 'B'
#     lenn = 2 * lenn + 3
oldlist = [1,3,1]
for i in range(2, n+1):
    oldlist = oldlist + [1] + oldlist
    oldlist[0] += 1
    oldlist[-1] += 1
# print(oldlist[0])
length = 0
answer = 0 
for i, item in enumerate(oldlist) : 
    if i % 2 == 0: # EVEN BUN
        length += item 
        
    else : #ODD PATTY 
        if length + item >= x: 
            answer += x - length 
        else : 
            answer += item 
        length += item 
    if length > x : 
        break 
# for i in range(x):
#     if b[i] == 'P':
#         answer += 1
# answer = b[:x].count('P')
print(answer)
