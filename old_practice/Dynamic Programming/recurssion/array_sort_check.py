# check if a given array is sorted or not

def check_sort(arr: list, index: int)->bool:
    # base call
    if index==1 or index ==0:
        return True
    # recursive call
    if (arr[0]<arr[1]) and (check_sort(arr[1:],index-1)):
        return True
    else:
        return False


if __name__=="__main__":
    lst = [1,2,3,4,5,9,6]
    print(f"List if sorted : {check_sort(lst, len(lst))}")