# Print all numbers from 1 to n and n to 1 in increasing/decreasing order respectively

def decreasing(n: int)->int:
    # base call
    if n == 0:
        return
    # recursion call
    print(n)
    decreasing(n-1)

def increasing(n: int)->int:
    # base call
    if n == 0:
        return
    # recursion call
    increasing(n-1)
    print(n)

if __name__=="__main__":
    decreasing(5)
    print("#################")
    increasing(5)