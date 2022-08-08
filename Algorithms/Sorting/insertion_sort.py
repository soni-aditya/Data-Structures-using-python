'''
This sorting algorithm maintains a sub-array that is always sorted. Values from the unsorted part of the array are placed at the correct position in the sorted part. It is more efficient in practice than other algorithms such as selection sort or bubble sort. Insertion Sort has a Time-Complexity of O(n2) in the average and worst case, and O(n) in the best case.

Example 

Here we sort the following sequence using the insertion sort
Sequence: 7, 2, 1, 6

    (7, 2, 1, 6) –> (2, 7, 1, 6), In the first iteration, the first 2 elements are compared, here 2 is less than 7 so insert 2 before 7.

    (2, 7, 1, 6) –> (2, 1, 7, 6), In the second iteration the 2nd and 3rd elements are compared, here 1 is less than 7 so insert 1 before 7.
    (2, 1, 7, 6) –> (1, 2, 7, 6), After the second iteration (1, 7) elements are not in ascending order so first these two elements are arranged. So, insert 1 before 2. 

    (1, 2, 7, 6) –> (1, 2, 6, 7), During this iteration the last 2 elements are compared and swapped after all the previous elements are swapped. 
'''


def insertionSort(lst):
    length = len(lst)

    for i in range(1, length):
        item = lst[i]
        # Move elements of lst[0 to i-1], which are greater to one position ahead of their current position
        j = i - 1
        while j >= 0 and item <= lst[j]:
            lst[j+1] = lst[j]
            j -= 1

        lst[j+1] = item
    return lst


if __name__ == '__main__':
    lst = [19, 2, 31, 45, 30, 11, 121, 27]

    print(insertionSort(lst))
