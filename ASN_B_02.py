#1.Function to sort an array using bubble sort.
  
def bubble_sort(array): 
    n = len(array) 
    for i in range(n-1):  
        for j in range(0, n-i-1):  
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j]               
    return array
print(bubble_sort([23,45,21,78,46,31]))



#2. Function for sorting array using selection sort.

def selection_sort(array):
    i = 0 
    n = len(array)
    for i in range(n-1):
        minpos = i
        for j in range(i,n):
            if array[j]< array[minpos]:
                minpos = j
        temp = array[i]
        array[i] = array[minpos]
        array[minpos] = temp    
    return array
print(selection_sort([1,5,3,6,2]))


  
    