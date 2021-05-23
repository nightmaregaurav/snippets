/*
 *   Created on: Feb 3, 2019
 *   Author: NightmareGaurav
 *   stack.h
 *
 * If you are reading this file as text, copy all code and save it as stack.h in your include folder(or any C header file directory on your environment).
 *
 * This header file will allow you to use three basic function of stack(using array).
 * push(char[]_Stack,int_address_of_stack_pointer,char_Item_to_push,const_int_maxsize); -> To push item in stack.
 * pop(char[]_Stack,int_address_of_stack_pointer,const_int_maxsize); -> To pop item from stack.(returns poped item).
 * traverse(char[]_Stack,int_address_of_stack_pointer,const_int_maxsize); -> To print current status of stack.
 *
 * A sample program is given at last of this file to demonstrate the usage
 *
 */
#include<stdio.h>
#include<stdlib.h>
	void push(char stack[], int *sp, char i, int const max){
		if(*sp==max)
			printf("\t\t\t\t\tOverflow.\n");
		else{
			*sp+=1;
			stack[*sp]=i;
			printf("\t\t\t\t\t%c is pushed to stack.\n",stack[*sp]);
		}
	}
	char pop(char stack[], int *sp, int const max){
		if(*sp==-1)
			printf("\t\t\t\t\tUnderflow.\n");
		else{
			printf("\t\t\t\t\tItem %c is poped.\n",stack[*sp]);
			*sp-=1;
			return(stack[*sp+1]);
		}
	}
	void traverse(char stack[], int *sp, int const max){
		int i;
		if(*sp==-1)
			printf("\t\t\t\t\t\tThere are no item in stack\n");
		else{
			printf("\t\t\t\t\tThe elements in Stack are:\n\n");
			for(i=*sp;i>=0;i--){
				printf("\t\t\t\t\t\t|\tstack[%d] = %c\t|\n",i,stack[i]);
				printf("\t\t\t\t\t\t+-----------------------+\n");
			}
		}
	}
/*
 * Sample program
 *
 *
#include<stdio.h>
#include "stack.h"
#define max 9
	void main(){
		int c, sp=-1;
		char e, stack1[max+1],i;
		do{
			printf("--*MENU*--\n\n\t1.Push data into stack.\n\t2.Pop data from stack\n\t3.View data of stack\n\t\tCurrent Stack Pointer=%d\n\t\t\tChoise: ",sp);
			scanf("%d",&c);
			getchar();
			switch(c){
				case 1:
					printf("\t\t\t\tInput Item To Push: ");
					scanf("%c",&i);
					getchar();
					push(stack1,&sp,i,max);
					break;
				case 2:
					pop(stack1,&sp,max);
					break;
				case 3:
					traverse(stack1,&sp,max);
					break;
				default:
					printf("\t\t\t\tWrong value entered.\n");
			}
			printf("Do you want to continue ?(Y/y for yes, anything else for no): ");
			scanf("%c",&e);
			getchar();
		}while(e=='y'||e=='Y');
		printf("Press anything to exit...");
		getchar();
	}
 *
 */