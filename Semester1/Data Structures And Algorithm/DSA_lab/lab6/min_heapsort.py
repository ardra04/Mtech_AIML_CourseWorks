
# Min Heapify
def Min_heapify(Arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and Arr[smallest] > Arr[left]:    #smallest so far is compared with left child
        smallest = left

    if right < n and Arr[smallest] > Arr[right]:       #smallest so far is compared with right child
        smallest = right
        
    if smallest!=i:                                       #change parent
        Arr[i], Arr[smallest] = Arr[smallest], Arr[i]
        Min_heapify(Arr, n, smallest)                            #recursive call

#Driver Code
Arr = [2,66,30,5,9,10]
n = len(Arr)




def heapSort(Arr):
    for i in range(n-1, 0, -1):
        # Swap
        Arr[i], Arr[0] = Arr[0], Arr[i]
        Min_heapify(Arr, i, 0)


# Build a Min heap
for i in range(n//2 - 1, -1, -1):
    Min_heapify(Arr, n, i)
heapSort(Arr)


#Display
print("Sorted Array is")
#print("Min heap is")
for i in range(n):
   print(Arr[i]),

