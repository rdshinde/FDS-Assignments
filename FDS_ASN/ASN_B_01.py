#1. Function for finding the element in an array using linear search.
def linear_search(size,array,target):
    i = 0
    while i<size:
        if array[i] == target:
            return i
        i+=1       
    return -1

#print(linear_search(9,[1,2,5,8,9,4,1,6,3],3)) # 9-> Size of array, 3-> Target element in array.

#2. Function for finding the element in an array using binary search.
def binary_search(array,target):
    start = 0
    end = len(array) - 1   
    while start<=end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1          
        elif array[mid] > target :
            end = mid - 1
        else :
            return mid
    return -1
output = binary_search([1,2,3,4,5,6,7,8,9],9)
print('Index position of target is: ',output)





'''def binary_search(start,end,array,target):
    if end >= start:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid 
        elif array[mid] > target:
            binary_search(start,mid-1,array,target)
        else:
            binary_search(mid+1,end,array,target)    
    else:
        return -1           
output = binary_search(0,5,[1,2,3,4,5],2)
if output != -1:
    print('Element  present at: ',str(output))
else:
    print('Element is not in array.')
        '''

