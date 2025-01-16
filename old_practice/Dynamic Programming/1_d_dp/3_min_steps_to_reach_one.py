'''
You are given a positive integer 'N'. You have to reduce it to one by performing following steps:
1. Reduce it to n-1 (n -> n-1)
2. If its divisible by 2, then divide it by 2(n -> n/2)
3. If its divisible by 3, then divide it by 2(n -> n/3)
'''
memo = {}
def dp(n):
    # base condition
    if n==1:
        return 0
    # memorization
    if n in memo: return memo[n]
    # recursion
    result = float('inf')
    if n%2==0:
        result = min(result, dp(n/2))
    if n%3==0:
        result = min(result, dp(n/3))
    result = min(result, dp(n-1))
    memo[n] = result+1
    return memo[n]


print(dp(10))

