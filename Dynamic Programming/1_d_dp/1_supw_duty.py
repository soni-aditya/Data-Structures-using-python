# find the minimum number of minutes spent in SUPW duty if a[1,2....i] and the duty ends on the ith day

'''
Nikhil has been designated SUPW coordinator. His task is to assign duties to students, including himself. The school's rules say that no student can go three days in a row without any SUPW duty

Nikhil wants to find an assignment of SUPW duty for himself that minimizes the number of minuted he spends overall on SUPW
'''
a = [2,2,3,2,2]
n = len(a)
dp = [-1 for i in a]

dp[0] = a[0]
dp[1] = a[1]
dp[2] = a[2]

for index in range(3,len(a)):
    dp[index] = min(dp[index-1],dp[index-2],dp[index-3])+ a[index]

print(min(dp[n-1],dp[n-2],dp[n-3]))

