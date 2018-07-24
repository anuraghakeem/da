#include<stdio.h>
#include<stdlib.h>
#define COMPARE(x,y) (((x)==(y))?0:((x)>(y))?1:-1)
typedef struct pnode
{
int coeff;
int exp;
struct pnode *link;
}*polypointer;

polypointer a,b,c;

void attach(int c,int e,polypointer *ptr)
{
polypointer temp;
temp=(polypointer)malloc(sizeof(*temp));
temp->coeff=c;
temp->exp=e;
(*ptr)->link=temp;
*ptr=temp;
}

void padd()
{
polypointer startA,lastC;
startA=a;
a=a->link;
b=b->link;
c=(polypointer)malloc(sizeof(struct pnode));
c->exp=-1;
lastC=c;
int sum=0,done=0;
do
{
switch(COMPARE(a->exp,b->exp))
{
case -1:attach(b->coeff,b->exp,&lastC);
        b=b->link;
        break;
case 0:if(startA==a)
       done=1;
       else
       {
       sum=a->coeff+b->coeff;
       if(sum) attach(sum,a->exp,&lastC);
       a=a->link;b=b->link;
       }
      break;
case 1:attach(a->coeff,a->exp,&lastC);
       a=a->link;
       break;
}
}while(!done);
lastC->link=c;
}

void input(int n,polypointer *ptr)
{
int c,e,i;
for(i=0;i<n;i++)
{
scanf("%d%d",&c,&e);
attach(c,e,ptr);
}
}

void display(polypointer ptr)
{
polypointer temp;
temp=ptr;
for(ptr=ptr->link;ptr!=temp;ptr=ptr->link)
printf("%dX^%d+",ptr->coeff,ptr->exp);
printf("\n");
}

void main()
{
int m,n;
polypointer lastA,lastB;
a=(polypointer)malloc(sizeof(struct pnode));
b=(polypointer)malloc(sizeof(struct pnode));
a->exp=-1;
b->exp=-1;
lastA=a;lastB=b;
printf("Enter the no. of terms for 1st polynomial\n");
scanf("%d",&m);
printf("Enter the coeff and exp of 1st\n");
input(m,&lastA);
lastA->link=a;
printf("Enter the no. of terms for 2nd polynomial\n");
scanf("%d",&n);
printf("Enter the coeff and exp of 2nd\n");
input(n,&lastB);
lastB->link=b;
printf("The first polynomial is\n");
display(a);
printf("The second polynomial is\n");
display(b);
padd();
printf("The resulting polynomial is\n");
display(c);
}
