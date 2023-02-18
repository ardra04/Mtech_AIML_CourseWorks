
# Max Heapify
def max_heapify(Arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and Arr[largest] < Arr[left]:    #largest so far is compared with left child
        largest = left

    if right < n and Arr[largest] < Arr[right]:       #largest so far is compared with right child
        largest = right
        
    if largest!=i:                                       #change parent
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        max_heapify(Arr, n, largest)                            #recursive call

#Driver Code
Arr = [2,66,30,5,9,10]
n = len(Arr)



def heapSort(Arr):
    for i in range(n-1, 0, -1):
        # Swap
        Arr[i], Arr[0] = Arr[0], Arr[i]
        max_heapify(Arr, i, 0)



# Build a max heap
for i in range(n//2 - 1, -1, -1):
    max_heapify(Arr, n, i)
heapSort(Arr)


#Display
print("Sorted Array is")
# print("Max heap is")
for i in range(n):
   print(Arr[i]),

