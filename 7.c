#include <stdio.h>
#include <stdlib.h>
typedef struct
{
        int key;
}element;
typedef struct node
{
        element data;
        struct node* link;
}*stackpointer;



stackpointer top[10]={NULL};

void push(element item, int i)
{
        stackpointer temp;
        temp=(stackpointer)malloc(sizeof(*temp));
        temp->data=item;
        temp->link=top[i];
        top[i]=temp;

}
element pop(int i)
{
        element item;
        stackpointer temp;
if(top[i]==NULL)
item.key = -1;

else
{
temp=top[i];
item = top[i]->data;
top[i] = top[i]->link;
free(temp);
}
        return item;


}
void display(int i)
{
        stackpointer temp;
if(top[i]==NULL)
printf("stack %d is empty\n",i);

else
{
temp = top[i];
printf(" stack %d is :\t",i);
while(temp)

{
printf("%d ->",temp->data.key);
temp=temp->link;
}
printf("NULL\n");
}
}
int main()
{
        int i, choice;
        element item;
        while(1)
        {
                printf("\nEnter 1. Insert 2. Delete 3. Display\n");
                scanf("%d",&choice);
                switch(choice)
                {
                case 1:
                        printf("Enter stack number: ");
                        scanf("%d",&i);
                        printf("Enter element to be inserted : ");
                        scanf("%d",&item.key);
                        push(item, i);
                        break;
            case 2:
                        printf("Enter stack number: ");
                        scanf("%d",&i);
                        item=pop(i);
                        if(item.key==-1)
printf("stack %d is empty\n",i);
else

                                printf("Element deleted %d", item.key);
                        break;
                case 3:
                        printf("Enter stack number: ");
                        scanf("%d",&i);
                        display(i);


                }
        }
}
