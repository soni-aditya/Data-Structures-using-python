'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact police if two adjacent houses are broken into on the same night

Given an array of integers (nums) representing the amount of money each house has, return the max amount of money that you can rob tonight without alerting the police

input: nums: [1,2,3,1]
output: 4

input: nums: [2,7,9,3,1]
output: 12
'''

def make_robbery(nums: list)->int:
    # base condition
    if len(nums)==0:
        return 0
    
    # recursion
    # state: f(i) = nums[i] + f(i+2)

    # if rob the current house
    rob = nums[0]+(make_robbery(nums[2:]) if len(nums)>2 else 0)
    # if not rob the current house
    not_rob = make_robbery(nums[1:]) if len(nums)>1 else 0

    max_robbery_amt = max(rob, not_rob)
    return max_robbery_amt

print(make_robbery([1,2,3,1]))
print(make_robbery([2,7,9,3,1]))
