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
}*queuepointer;



queuepointer front[10]={NULL}, rear[10]={NULL};

void insert(element item, int i)
{
        queuepointer temp;
        temp=(queuepointer)malloc(sizeof(*temp));
        temp->data=item;
        temp->link=NULL;
        if(front[i]!=NULL)
rear[i]->link = temp;
else
front[i]=temp;

rear[i]=temp;

}
element deleteq(int i)
{
        element item;
        queuepointer temp;
if(front[i]==NULL)
{
item.key=-1;

}
else
{
temp=front[i];
item = temp->data;
front[i]=front[i]->link;
free(temp);
}

        return item;

}

void display(int i)
{

queuepointer temp;


if(front[i]==NULL)
printf(" queue %d is empty\n",i);

else
{
temp = front[i];
printf(" queue %d\t",i);
while(temp!=NULL)
{
printf("%d -> ",temp->data.key);
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
                        printf("Enter queue index: ");
                        scanf("%d",&i);
                        printf("Enter element to be inserted : ");
                        scanf("%d",&item.key);
                        insert(item, i);
                        break;
  case 2:
                        printf("Enter queue index: ");
                        scanf("%d",&i);
                        item=deleteq(i);
                        if(item.key==-1)
                         printf("queue %d is empty\n",i);
                                else
                                printf("Element deleted %d", item.key);
                        break;
                case 3:
                        printf("Enter queue index: ");
                        scanf("%d",&i);
                        display(i);


                }
        }
}
