#include<stdio.h>
typedefenum{lparen,rparen,plus,minus,times,divide,mod,eos,operand}precedence;
charexpr[100];
intstack[100];
inttop=-1;
voidpush(inti)
{
stack[++top]=i;
}
intpop()
{
returnstack[top--];
}
precedenceget_token(char*symbol,int*n)
{
*symbol=expr[(*n)++];
switch(*symbol)
{
case'(':returnlparen;
case')':returnrparen;
case'+':returnplus;
case'-':returnminus;
case'*':returntimes;
case'/':returndivide;
case'%':returnmod;
case'\0':returneos;
default:returnoperand;
}
}
voidmain()
{
intn=0,op1,op2;
charsymbol;
precedencetoken;
printf("Enterapostfixexpr:");
scanf("%s",expr);
for(token=get_token(&symbol,&n);token!=eos;token=get_token(&symbol,&n))
{
if(token==operand)
push(symbol-'0');
else
{
op2=pop();
op1=pop();
switch(token)
{
caseplus:push(op1+op2);break;
caseminus:push(op1-op2);break;
casetimes:push(op1*op2);break;
casedivide:push(op1/op2);break;
}
}
}
printf("Answer:%d\n",pop());
}
