
astr = input()
bstr = input()
# print(astr, bstr)

astr, bstr = '0'+astr, '0'+bstr

dp = [0] * 1001
dp2 = [0] * 1001

for j in range(1,len(bstr)):
    for i in range(1,len(astr)):
        if astr[i] == bstr[j] : 
            dp[i] = dp2[i-1]+1
        else : 
            dp[i] = max(dp[i-1], dp2[i])
    dp2 = dp[:]
    
print(max(dp2))
