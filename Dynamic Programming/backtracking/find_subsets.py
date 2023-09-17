# given a string, find all subsets of given string 
## input: abc
## output: "", a,b,c,ab,ac,bc,abc


def find_subsets(inp: list)-> list:
    results = []

    subset = []
    def depth_first_search(index):
        # base case
        if index >= len(inp):
            results.append(subset.copy())
            return
        # include inp[i]
        subset.append(inp[index])
        depth_first_search(index+1)
        # exclude the inp[i]
        subset.pop()
        depth_first_search(index+1)
    depth_first_search(0)
    print(results)

find_subsets(inp=['a','b','c'])