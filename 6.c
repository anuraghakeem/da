#include<stdio.h>
#include<stdlib.h>
#define max_stack_size  100
#define max_expr_size  100
typedef enum
{
    lparen, rparen, plus, minus, times, divide, mod, eos, operand
    
} precedence;



int isp[] = {0, 19, 12, 12, 13, 13, 13, 0};
int icp[] = {20, 19, 12, 12, 13, 13, 13, 0};


int top = -1;

char expr[max_expr_size];
int stack[max_stack_size];



void push(int x)
{
stack[++top] = x;
}


int pop()
{
return stack[top--];
}


precedence get_token(char* symbol, int* n)
{
*symbol = expr[(*n)++];
switch(*symbol)
{
case '(': return lparen;
case ')': return rparen;
case '+': return plus;
case '-': return minus;
case '/': return divide;
case '*': return times;
case '%': return mod;
case '\0': return eos;
default: return operand;
}
}


int eval()
{
precedence token;
char symbol;
int op1, op2;
int n = 0;
top = -1;
token = get_token(&symbol, &n);
while(token!=eos)
{
if(token==operand) push(symbol-'0');
else{
op2 = pop();
op1 = pop();

switch(token)
{
case plus: push(op1+op2); break;
case minus: push(op1-op2); break;
case times: push(op1*op2); break;
case divide: push(op1/op2); break;
case mod: push(op1%op2);
}

}
token = get_token(&symbol, &n);
}
return pop();
}

int main()
{
    printf("Enter the expression:\n");
        scanf("%s", expr);
        printf("The value of the expression is: %d\n", eval());
        
return 0;
}
