#include<stdio.h>
#include<stdlib.h>
typedefstruct{
intkey;
}element;
typedefstructnode{
elementdata;
structnode*link;
}*stackpointer;
stackpointertop[20];
elementstackEmpty()
{
elemente;
e.key=-999;
printf("StackisEmpty\n");
returne;
}
voidpush(inti,elementitem)
{
stackpointertemp=(stackpointer)malloc(sizeof(*temp));
temp->data=item;
temp->link=top[i];
top[i]=temp;
}
elementpop(inti)
{
stackpointertemp=top[i];
if(!temp)

returnstackEmpty();
elementitem;
item=top[i]->data;
top[i]=top[i]->link;
free(temp);
returnitem;
}
voiddisplay(inti)
{
stackpointertemp=top[i];
if(!temp)
stackEmpty();
else{
printf("Stack[%d]:",i);
while(temp)
{
printf("%d->",temp->data.key);
temp=temp->link;
}
printf("NULL\n");
}
}
intmain()
{
intn,i,choice;
elementitem;
printf("Enterthenumberofstacks:");
scanf("%d",&n);

for(i=0;i<n;i++)
top[i]=NULL;
while(1)
{
printf("1.Push\n2.pop\n3.Display\n");
scanf("%d",&choice);
switch(choice)
{
case1:
printf("Enterthestackno.andelementtopush:");
scanf("%d%d",&i,&item.key);
push(i,item);
break;
case2:
printf("Enterthestackno.topop:");
scanf("%d",&i);
item=pop(i);
if(item.key!=-999)
printf("Elementpopedis%d\n",item.key);
break;
case3:
printf("Enterthestackno.todisplay:");
scanf("%d",&i);
display(i);
break;
default:
exit(0);
}

}
}
