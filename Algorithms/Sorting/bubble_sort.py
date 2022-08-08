'''
Bubble Sort is a simple sorting algorithm. This sorting algorithm repeatedly compares two adjacent elements and swaps them if they are in the wrong order. It is also known as the sinking sort. It has a time complexity of O(n2) in the average and worst cases scenarios and O(n) in the best-case scenario. Bubble sort can be visualized as a queue where people arrange themselves by swapping with each other so that they all can stand in ascending order of their heights. Or in other words, we compare two adjacent elements and see if their order is wrong, if the order is wrong we swap them. (i.e arr[i] > arr[j] for 1 <= i < j <= s; where s is the size of the array, if array is to be in ascending order, and vice-versa).

Example -------------------------------------------------

Here we sort the following sequence using bubble sort
Sequence: 2, 23, 10, 1

First Iteration

    (2, 23, 10, 1) –> (2, 23, 10, 1), Here the first 2 elements are compared and remain the same because they are already in ascending order.
    (2, 23, 10, 1) –> (2, 10, 23, 1), Here 2nd and 3rd elements are compared and swapped(10 is less than 23) according to ascending order.
    (2, 10, 23, 1) –> (2, 10, 1, 23), Here 3rd and 4th elements are compared and swapped(1 is less than 23) according to ascending order
    At the end of the first iteration, the largest element is at the rightmost position which is sorted correctly.

Second Iteration

        (2, 10, 1, 23) –> (2, 10, 1, 23), Here again, the first 2 elements are compared and remain the same because they are already in ascending order.
        (2, 10, 1, 23) –> (2, 1, 10, 23), Here 2nd and 3rd elements are compared and swapped(1 is less than 10) in ascending order.
        At the end of the second iteration, the second largest element is at the adjacent position to the largest element.

and so on........
'''


def bubbleSort(lst):
    length = len(lst)

    # For loop to traverse through all elements in an array
    for i in range(length):
        # In first iteration, the largest element would go to the end index(thus we don't need to visit
        # last index from second iteration onwards)
        # similarly, second largest element would go to second last index by seccond iteration (in worst case scenario)
        # thus we take range(n-i-1) for next loop through
        for j in range(length-i-1):
            # Swap the elements if the element found is greater than the adjacent element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


if __name__ == '__main__':
    lst = [19, 2, 31, 45, 30, 11, 121, 27]

    print(bubbleSort(lst))
