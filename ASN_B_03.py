#1. Function to create partition in an array.
def partition(array, low, high):
    i = (low-1)         # index of smaller element
    pivot = array[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if array[j] <= pivot:
            # increment index of smaller element
            i = i+1
            array[i], array[j] = array[j], array[i]
 
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)


#2. Function to perform quick sort operation on an array.
def quick_sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(array, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)
    return array

print(quick_sort([4,3,7,2,9,0,8,1],0,7))
