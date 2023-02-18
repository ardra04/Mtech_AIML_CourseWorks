def insertionsort(a):
    n=len(a)
    for i in range(1,n):
        val=a[i]
        pos=i
        while pos>0 and a[pos-1]>val:
            a[pos]=a[pos-1]
            pos=pos-1
            a[pos]=val
            
a = [10,4,3,9,11]
print('Original array :', a)
insertionsort(a)
print('Sorted Array :',a)


#compare and swap smallest to front. (10,4), (10,3),(3,4),...