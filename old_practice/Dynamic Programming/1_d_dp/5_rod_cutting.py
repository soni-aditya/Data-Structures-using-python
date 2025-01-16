'''
Given a rod of length n and array prices of length n denoting the cost of pieces of the rod of length 1 to n, find the maximum amount that can be made if the rod is cut up optimally

ie. if n=8
and prices = [1,3,4,5,7,9,10,11] ie.  price of cutting rod into piece of 2 is 3 (1th index)

if n = 4
and prices = [1,1,1,6]
the output will be 6 in this case
'''
memory= {}

def rod_cutting(n:int, prices:list)-> int:
    # base condition
    if n<=0:
        return 0
    # recursion
    if n in memory:
        return memory[n]
    
    price = 0
    for length in range(1,n+1):
        price = max(price, prices[length-1]+rod_cutting(n-length,prices))
    
    memory[length] = price
    return price
    

N = 8
prices = [1,3,4,5,7,9,10,11]
print(rod_cutting(N,prices))

# space complexity: O(1)
# time complexity: O(n*n) because of loop inside the recursive call