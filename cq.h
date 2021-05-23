/*
 *   Created on: Feb 19, 2019
 *   Author: NightmareGaurav
 *   cq.h
 *
 * If you are reading this file as text, copy all code and save it as cq.h in your include folder(or any C header file directory on your environment).
 * Write #include"cq.h" in program if this file is in working directory or use #include<cq.h> if this is in system's(compiler's) header file directory.
 *
 * This header file will allow you to use three basic function in circular queue(using array).
 * incqueue(char_data,char[]_queue,int_address_of_front,int_address_of_rear,int_const_max); -> To add item in queue.
 * decqueue(char[]_queue,int_address_of_front,int_address_of_rear,int_const_max); -> To delete item from queue.(returns removed item).
 * cqtraverse(char[]_queue,int_address_of_front,int_address_of_rear,int_const_max); -> To print current status of queue.
 *
 * A sample program is given at last of this file to demonstrate the usage
 *
 */
#include<stdio.h>
	int isbetween(int a, int f, int r, int const max){
		do{
			if(f==a||r==a)
				return 1;
			else if(f==r)
				return 0;
			else if(f==-1&&r==-1)
				return 0;
			else
				f=(f+1)%max;
		}while(f!=r);
		return 0;
	}
	void incqueue(char data,char queue[],int *f, int *r, int const max){
		if(*f==(*r+1)%max)
			printf("\t\t\t\t\tQueue full...\n");
		else{
			if(*f==*r&&*r==-1){
				*r=0;
				*f=0;
			}
			else
				*r=++*r%max;
			queue[*r]=data;
			printf("\t\t\t\t\t%c Inqueued...\n",data);
		}
	}
	char decqueue(char queue[], int *f, int *r, int const max){
		char temp;
		if(*f==-1)
			printf("\t\t\t\t\tQueue empty...\n");
		else{
			temp=queue[*f];
			if(*f==*r)
				*f=*r=-1;
			else
				*f=++*f%max;
			printf("\t\t\t\t\t%c dequeued...\n",temp);
			return(temp);
		}
		return('\0');
	}
	void cqtraverse(char queue[], int *f, int *r, int const max){
		int s,a;
		printf("\t\t\t\t\tThe elements in Queue are:\n\n");
		printf("\t\t\t\t\t\t\t   .>>>>>>>>>>>>>>>>>>.\n");
		printf("\t\t\t\t\t\t\t   |.>>>>>>>>>>>>>>>>.|\n");
		printf("\t\t\t\t\t\t\t   ||   \t    \\./\n");
		printf("\t\t\t\t\t\t\t  ~^^~  \t    \\./\n");
		printf("\t\t\t\t\t\t+-----------------------+   \\./\n");
		a=0;
		for(s=max-1;s>=0;s--){
			if(queue[s]=='\0')
				printf("\t\t\t\t\t\t|\tQueue[%d] = NULL\t|   \\./\n",s,queue[s]);
			else if(isbetween(s,*f,*r,max))
				printf("\t\t\t\t\t\t|\tQueue[%d] = %c\t|   \\./\n",s,queue[s]);
			else{
				printf("\t\t\t\t\t\t|\t*Queue[%d] = %c\t|   \\./\n",s,queue[s]);
				a=1;
			}
			printf("\t\t\t\t\t\t+-----------------------+   \\./\n");
		}
		printf("\t\t\t\t\t\t\t  ~^^~  \t    \\./\n");
		printf("\t\t\t\t\t\t\t   ||   \t    \\./\n");
		printf("\t\t\t\t\t\t\t   |.<<<<<<<<<<<<<<<<.|\n");
		printf("\t\t\t\t\t\t\t   .<<<<<<<<<<<<<<<<<<.\n");
		printf("\n\t\t\t\t\t\tCurrent Front: %d, Rear: %d.\n",*f,*r);
		if(a)
			printf("\t\t\t\t* Denotes item which front and rear don't cover.(Deleted).");
		printf("\n\n");
	}
/*
 * Sample program
 *
 *
#include<stdio.h>
#include"cq.h"
#define max 5
	void main(){
		int c, f=-1, r=-1;
		char e, queue1[max]="",i;
		do{
			printf("--*MENU*--\n\n\t1.Inqueue\n\t2.Dequeue\n\t3.Traverse\n\t\tCurrent Front=%d, Rear=%d\n\t\t\tChoise: ",f,r);
			scanf("%d",&c);
			getchar();
			switch(c){
				case 1:
					printf("\t\t\t\tInput Item To Inqueue: ");
					scanf("%c",&i);
					getchar();
					incqueue(i,queue1,&f,&r,max);
					break;
				case 2:
					decqueue(queue1,&f,&r,max);
					break;
				case 3:
					cqtraverse(queue1,&f,&r,max);
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
