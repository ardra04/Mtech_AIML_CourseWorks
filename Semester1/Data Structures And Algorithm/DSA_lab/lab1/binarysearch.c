#include <stdio.h>
int main()
{
int  low, high, mid;

    int i,key=10;
	int array[] = { 2, 3, 4, 10, 40 };
	int n = sizeof(array) / sizeof(array[0]);


low = 0;
high = n - 1;
mid = (low+high)/2;


while (low <= high) {

if(array[mid] < key){
low = mid + 1;
mid = (low+high)/2;
}

else if (array[mid] == key) {
printf("%d found at index %d", key, mid);
break;
}

else{
high = mid - 1;
mid = (low + high)/2;
}

}


if(low > high){
printf("Not found! %d isn't present in the list", key);
}

return 0;
}




//binary search works in sorted array 
//low - 1st element
//high - last element
// mid -  (low+high)/2
//check   key<mid  or  >mid  or  =mid