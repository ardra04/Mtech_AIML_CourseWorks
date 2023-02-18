def partition(array, low, high):
  pivot = array[high]            # rightmost element [ ] pivot
  i = low - 1                    # pointer for greater element
  for j in range(low, high):
    if array[j] <= pivot:            # if element smaller than pivot is found, swap it with the greater element pointed by i
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])                 # swapping element at i with element at j
  (array[i + 1], array[high]) = (array[high], array[i + 1])       
  return i + 1                                                    # return the position from where partition is done


def quickSort(array, low, high):
  if low < high: 
    pi = partition(array, low, high)   #elements smaller than pivot on left and larger on right
    quickSort(array, low, pi - 1)     # recursive call on the left of pivot
    quickSort(array, pi + 1, high)    # recursive call on the right of pivot
 

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array =  " , data)
quickSort(data, 0, len(data) - 1)
print('Sorted Array  = ', data)






#first element -pivot
#less than pivot on 1 side 
#greater on other side...