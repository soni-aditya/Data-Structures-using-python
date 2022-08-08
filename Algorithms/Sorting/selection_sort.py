'''
This sorting technique repeatedly finds the minimum element and sort it in order. Bubble Sort does not occupy any extra memory space, but insertion sort does. During the execution of this algorithm, two subarrays are maintained, the subarray which is already sorted, and the remaining subarray which is unsorted. During the execution of Selection Sort for every iteration, the minimum element of the unsorted subarray is arranged in the sorted subarray. Selection Sort is a more efficient algorithm than bubble sort. Sort has a Time-Complexity of O(n2) in the average, worst, and in the best cases.

Example 

Here we sort the following sequence using the selection sort
Sequence: 7, 2, 1, 6

    (7, 2, 1, 6) –> (1, 7, 2, 6), In the first traverse it finds the minimum element(i.e., 1) and it is placed at 1st position.

    (1, 7, 2, 6) –> (1, 2, 7, 6), In the second traverse it finds the 2nd minimum element(i.e., 2) and it is placed at 2nd position.

    (1, 2, 7, 6) –> (1, 2, 6, 7), In the third traverse it finds the next minimum element(i.e., 6) and it is placed at 3rd position.

After the above iterations, the final array is in sorted order, i.e., 1, 2, 6, 7
'''


def selectionSort(lst):
    length = len(lst)

    for i in range(length):
        min_value_index = i

        for j in range(i+1, length):
            # if the index has value less than the value at min value index, we consider current index as
            # min value index and assign its value to min_value_index variable
            if lst[j] < lst[min_value_index]:
                min_value_index = j

        # now that we found our min value index in the whole sub list, we arrange it to its correct location
        lst[i], lst[min_value_index] = lst[min_value_index], lst[i]

    return lst


if __name__ == '__main__':
    lst = [19, 2, 31, 45, 30, 11, 121, 27]

    print(selectionSort(lst))
