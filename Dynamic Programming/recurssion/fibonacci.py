def fibonacci(index: int)->int:
    # base case
    if (index == 0) or (index == 1):
        return index
    # recursion case
    return fibonacci(index-1)+fibonacci(index-2)

if __name__=="__main__":
    n = 11
    print(f"Fibonacci if {n} : {fibonacci(n)}")