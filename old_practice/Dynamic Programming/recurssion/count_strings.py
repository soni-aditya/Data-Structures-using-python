# count the number of binary strings with no consecutive ones that can be
# formed using a binary string of length N
# input: N

def find_ways(n: int)-> int:
    # print(n)
    if n==0:
        return 1
    if n==1:
        return 2
    else:
        return find_ways(n-1) + find_ways(n-2)

print(find_ways(4))
    
    