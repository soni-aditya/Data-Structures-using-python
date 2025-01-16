# write a function to generate all possinle n pairs of balanced parantheses '(' and ')'
## input: 2
## output: ()(), (())

def generate_brackets(output: str, n: int, open: int, close: int, current_index: int):
    # base case
    if current_index == 2*n:
        print(output)
        print()
    # recursive call
    # place open bracket
    if open<n:
        generate_brackets(output+"(",n,open+1,close, current_index+1)
    # place closing bracket
    if close<open:
        generate_brackets(output+')',n,open, close+1, current_index+1)
        

N = int(input("Enter value of n:"))
generate_brackets("",N,0,0,0)
