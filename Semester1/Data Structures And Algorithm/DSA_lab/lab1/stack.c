//stack -LIFO

#include<stdio.h>
#define stackCapacity 5

int stack[stackCapacity], top=-1;
void push(int);
int pop(void);
int isFull(void);
int isEmpty(void);
void traverse(void);
void atTop(void);



void main(void)
{
    int choice, stackItem;
    while(1){
        printf("\n Stack Operations");
        printf("\n 1.  Push");
        printf("\n 2.  Pop");
        printf("\n 3.  Return SackTop");
        printf("\n 4.  Traverse");
        printf("\n 5.  Quit");
        printf("\n Enter your choice : ");
        scanf("%d",&choice);
        

        switch(choice){
            case 1:
                    printf("Enter a integer value to push it on to stack : ");
                    scanf("%d",&stackItem);
                    push(stackItem);
                    break;
            case 2:
                    stackItem = pop();
                    if(stackItem == 0){
                        printf("Your stack is underflow");
                    }else{
                        printf("Last popped item : %d", stackItem);
                    }
                    break;
            case 3:
                    atTop();
                    break;
            case 4:
                    traverse();
                    break;
            case 5:
                    return;
                    break;
            default: printf("Please enter correct choice : ");
        }
    }
}

//Push
void push(int stackElement)
{
    if(isFull()){
        printf("Stack is full.It can't be overflowed.");
    }else{
        top++;
        stack[top] = stackElement;
        printf("%d has been pushed", stackElement);
    }
}

//Check if stack is full?
int isFull(){
    if(top == stackCapacity-1){
        return 1;
    }else{
        return 0;
    }
}


//Check if stack is empty
int isEmpty(){
    if(top == -1){
        return 1;
    }else{
        return 0;
    }
}

//Pop last element
int pop(){
    if(isEmpty()){
        return 0;
    }else{
        return stack[top--];
    }
}

//Return topmost element
void atTop()
{
    if(isEmpty())
    {
        printf("Your Stack is empty");
    }else{
        printf("Element at top is : %d", stack[top]);
    }
}

//Output all
void traverse(){
    if(isEmpty())
    {
        printf("Stack is empty");
    }else{
        int i;
        printf("\n Stack Elements are : ");
        for(i=0; i <= top; i++){
            printf("%d ", stack[i]);
        }
    }
   
}