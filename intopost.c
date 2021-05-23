#include<stdio.h>
#include<string.h>
#include"stack.h"
#define max 19
	int compare(char a, char b){
		if(a=='$')
			return 0;
		else if((a=='*' || a=='/') && b!='$')
			return 0;
		else if(a==b)
			return 0;
		else if(a=='*' && b=='/')
			return 0;
		else if(a=='/' && b=='*')
			return 0;
		else if(a=='+' && b=='-')
			return 0;
		else if(a=='-' && b=='+')
			return 0;
		else
			return 1;
	}
	void main(){
		char expression[20]="", opstack[20]="", converted[20]="",temp;
		int i, opsp=-1,cosp=-1;
		printf("Give the infix expression: ");
		scanf("%s",expression);
		for(i=0;i<strlen(expression);i++){
			if(expression[i]=='(')
				push(opstack,&opsp,expression[i],max);
			else if(expression[i]=='+'||expression[i]=='-'||expression[i]=='*'||expression[i]=='/'||expression[i]=='$'){
				if(opsp==-1)
					push(opstack,&opsp,expression[i],max);
				else if(opstack[opsp]=='(' || compare(opstack[opsp],expression[i]))
					push(opstack,&opsp,expression[i],max);
				else{
					push(converted,&cosp,pop(opstack,&opsp,max),max);
					push(opstack,&opsp,expression[i],max);
				}
			}
			else if(expression[i]==')'){
				do{
					push(converted,&cosp,temp=pop(opstack,&opsp,max),max);
				}while(temp!='(');
				pop(converted,&cosp,max);
			}
			else
				push(converted,&cosp,expression[i],max);
			printf("postfix stack:\n");
			traverse(converted,&cosp,max);
			printf("operation stack:\n");
			traverse(opstack,&opsp,max);
		}
		while(opsp!=-1)
			push(converted,&cosp,pop(opstack,&opsp,max),max);
		printf("postfix stack:\n");
		traverse(converted,&cosp,max);
		printf("operation stack:\n");
		traverse(opstack,&opsp,max);
		printf("\n\nSo, Corresponding postfix expression of %s is: %s\n",expression,converted);
	}
