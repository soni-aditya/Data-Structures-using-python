# find the power of a given number (complexity: n)

def power(num: int,n: int)->int:
    # base case
    if n==0:
        return 1
    # recursion call
    return num * power(num, n-1)

print(f"3 raise to the power 5 : {power(5,3)}")


# do the above function in optimized manner (complexity: log(n))
def fast_power(num: int,n: int)->int:
    # base case
    if n==0:
        return 1
    # recursion call
    sub_prob = fast_power(num, n//2)
    sub_prob_square = sub_prob*sub_prob
    if n&1:
        return num*sub_prob_square
    else:
        return sub_prob_square
    
print(f"3 raise to the power 5 : {fast_power(5,3)}")