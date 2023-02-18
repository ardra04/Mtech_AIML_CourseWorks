#include<stdio.h>
int main()
{
    int i,key=10;
	int a[] = { 2, 3, 4, 10, 40 };
	int size = sizeof(a) / sizeof(a[0]);

    for(i=0;i<size;++i)
        if(a[i]==key)
            break;
     
    if(i<size)
        printf("Element found at index %d",i);
    else
        printf("Element not found");
  
    return 0;
}


//here we are sequentially checking key with each array elements  -O(n)


