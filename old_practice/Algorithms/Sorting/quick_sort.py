'''
Just unlikely merge Sort, QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

- Always pick the first element as a pivot
- Always pick the last element as a pivot
- Pick a random element as a pivot
- Pick median as a pivot

Here we will be picking the last element as a pivot. The key process in quickSort is partition(). Target of partitions is, given an array and an element ‘x’ of array as a pivot, put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time. 
'''
'''
Pseudo Code: Recursive QuickSort function 

// low  --> Starting index,
// high  --> Ending index

        quickSort(arr[], low, high) {

            // Till starting index is lesser than ending index
            if (low < high) {

                // pi is partitioning index,
                // arr[p] is now at right place
                pi = partition(arr, low, high);

                // Before pi
                quickSort(arr, low, pi - 1);
                // After pi
                quickSort(arr, pi + 1, high);
            }
        }
'''
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.


def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums


example = [4, 5, 1, 2, 3]
print(quicksort(0, len(example)-1, example))

example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
# As you can see, it works for duplicates too
print(quicksort(0, len(example)-1, example))


'''
Time Complexity: Worst case time complexity is O(N2) and average case time complexity is O(N logN)
Auxiliary Space: O(1)
'''
