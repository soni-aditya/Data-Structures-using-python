def fact(num: int) -> int:
    # base condition
    if num == 0:
        return 1
    # recursion case
    return num * fact(num-1)

if __name__ =='__main__':
    n = 5
    print(f"Factorial of {n} :{fact(5)}")