#include<stdio.h>
#include<stdlib.h>
typedefstructnode
{
structnode*llink;
intdata;
structnode*rlink;
}*nodepointer;
nodepointerh_node,last;
voidinsert_node(intn)
{
nodepointertemp=(nodepointer)malloc(sizeof(*temp));
temp->data=n;
last->rlink=temp;
temp->llink=last;
temp->rlink=h_node;
h_node->llink=temp;
last=temp;
}
nodepointersearch(intn)
{
nodepointertemp=h_node->rlink;
while(temp!=h_node)
{
if(temp->data==n)
returntemp;
temp=temp->rlink;
}
returnNULL;
}
voiddelete_node(intn)
{
nodepointertemp=search(n);
if(temp==NULL)
printf("Enteredelementnotfound\n");
else
{
temp->llink->rlink=temp->rlink;
temp->rlink->llink=temp->llink;
printf("Element%ddeletedfromthelist\n",temp->data);
free(temp);
}
}
voiddisplay_fwd()
{
nodepointertemp=h_node->rlink;
while(temp!=h_node)
{
printf("%d",temp->data);
temp=temp->rlink;
}
printf("\n");
}
voiddisplay_bwk()
{
nodepointertemp=h_node->llink;

while(temp!=h_node)
{
printf("%d",temp->data);
temp=temp->llink;
}
printf("\n");
}
voidmain()
{
intn,choice;
h_node=(nodepointer)malloc(sizeof(*h_node));
h_node->llink=h_node->rlink=h_node;
last=h_node;
while(1)
{
if(h_node->rlink==h_node)
last=h_node;
printf("1.Insert\n2.Delete\n3.Displayfwd\n4.Displaybwk\n");
scanf("%d",&choice);
switch(choice)
{
case1:
printf("Entertheelementtoinsert:");
scanf("%d",&n);
insert_node(n);
break;
case2:
if(h_node->rlink==h_node||h_node->llink==h_node)
printf("Thelistisempty\n");
else
{
printf("Entertheelementtodeleted:");
scanf("%d",&n);
delete_node(n);
}
break;
case3:
display_fwd();
break;
case4:
display_bwk();
break;
default:
exit(0);
}
}
}
