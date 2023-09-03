totalWays = 0
def find_ways(c: str, total: int, sum: int = 0):
    global totalWays
    if total == 0:
        return 
    
    else:
        find_ways(c, total, sum+1)
        find_ways(c, total, sum+2)
        find_ways(c, total, sum+3)

find_ways({1,2,3},5,0)
print(totalWays)
