#include<stdio.h>
#include<stdlib.h>
	struct node{
		char data;
		struct node *ptr;
	}*head;
	int nodescount=0;
	void dis(){
		if(head!=NULL){
		struct node *tem;
		tem = head;
			do{
				printf("\t%c | %p\n",tem->data,tem->ptr);
				tem = tem->ptr;
			}while(tem!=NULL);
			printf("Total nodes: %d\n",nodescount);
		}
	}
	void create(){
		int i;
		printf("Input Position: ");
		scanf("%d",&i);
		getchar();
		if(i <= 0 || i > (nodescount+1)){
			printf("Error in input...");
			return;
		}
		else if(i == 1){
			struct node *t;
			t = head;
			head = (struct node*) malloc(sizeof(struct node));
			if(head==NULL){
				printf("Memory allocation completed with problem...\n");
				return;
			}
			else{
				printf("Memory allocation completed successfully...\n");
				printf("Input: ");
				scanf("%c",&head->data);
				getchar();
				head->ptr = t;
				nodescount++;
			}
		}
		else{
			struct node *tem,*t;
			tem = head;
			while(i > 2){
				tem = tem->ptr;
				i--;
			}
			t=tem->ptr;
			tem->ptr = (struct node*) malloc(sizeof(struct node));
			if(tem->ptr==NULL){
				printf("Memory allocation completed with problem...\n");
				tem->ptr = t;
				return;
			}
			else{
				printf("Memory allocation completed successfully...\n");
				printf("Input: ");
				scanf("%c",&tem->ptr->data);
				getchar();
				tem->ptr->ptr=t;
				nodescount++;
			}
		}
	}
	char destroy(){
		char a;
		int i;
		printf("Input Position: ");
		scanf("%d",&i);
		getchar();
		printf("I am here...");
		if(i<=0 || i>nodescount){
			return('\0');
		}
		else if(head!=NULL){
			struct node *tem,*t;
			tem = head;
			do{
				t = tem;
				tem = tem->ptr;
				i--;
			}while(i > 1);
			tem = tem->ptr;
			a = t->ptr->data;
			free(t->ptr);
			if(t->ptr != NULL){
				printf("Failed to destroy allocated memory space...");
				return('\0');
			}
			else{
				t->ptr=tem;
				printf("Successfully destroyed allocated location for %c...",a);
				return(a);
			}
		}
		else{
			printf("List is already empty...");
			return('\0');
		}
	}
	void main(){
		char c;
		int ch;
		do{
			printf("Input:\n1. To input.\n2. To delete.\n3. To display.\n\t\tChoise: ");
			scanf("%d",&ch);
			getchar();
			switch(ch){
				case 1:
					create();
					break;
				case 2:
					destroy();
					break;
				case 3:
					dis();
					break;
				default:
					printf("Wrong input...\n");
			}
			//printf("Do you wish to continue ?(Y/y for yes, anything else for no): ");
			//scanf("%c",&c);
			//getchar();
		}while(1);
	}
