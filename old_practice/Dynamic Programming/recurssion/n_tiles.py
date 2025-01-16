# in how many ways can you fill a floor of size 4xn with tiles of size 4x1

def find_ways(n: int)->int:
    # base case
    if n<4:
        return 1
    # recursion
    return find_ways(n-1)+find_ways(n-4)

print(find_ways(10))