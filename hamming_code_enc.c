#include<stdio.h>
#include<string.h>

int verify(char data[5]){
	int i1=0,i0=0;
	if(strlen(data)!=4){
		printf("Invalid data length: %d",strlen(data));
		return 0;
	}
	else{
		for(int i=0;i<4;i++){
			if(data[i]=='1')
				i1++;
			else if(data[i]=='0')
				i0++;
		}
		if(i0+i1!=4){
			printf("Data contains invalid character.");
			return 0;
		}
		else
			return 1;
	}
}
void printHamming(int data[5],int parity[4],int len){
	printf("\t\t\t.............................\n");
	if(len == 4)
		printf("\t\t\t| %d | %d | %d |   | %d |   |   |\n",data[0],data[1],data[2],data[3]);
	else
		printf("\t\t\t| %d | %d | %d | %d | %d | %d | %d |\n",data[0],data[1],data[2],parity[0],data[3],parity[1],parity[2]);
	printf("\t\t\t'---------------------------'\n");
	printf("\t\t          ^   ^   ^   ^   ^   ^   ^\n");
	printf("\t\t\t D-7 D-6 D-5 P-4 D-3 P-2 P-1\n");
}
void main(){
	char tempData[5],Type[5],Type0[5];
	int data[5],parity[4],type,condition;
	printf("Input the 4 bit data: ");
	scanf("%s",&tempData);
	printf("Parity type(Even=0/Odd=1): ");
	scanf("%d",&type);
	if(type>1 || type<0){
		printf("Invalid Parity type given, Selecting 'Even' by default.\n");
		type = 0;
	}
	if(type)
		strcpy(Type,"Odd");
	else
		strcpy(Type,"Even");
	if(verify(tempData)){
		for(int i=0;i<4;i++)
			if(tempData[i]=='1')
				data[i] = 1;
			else
				data[i] = 0;
		printf("\n\n===========> Hamming code Using %s Parity System on Data: %d%d%d%d <===========",Type,data[0],data[1],data[2],data[3]);
		printf("\nAs we are given the 4 data bits:\n");
		printHamming(data,parity,4);
		printf("Firstly,\n\tWe need to Find Parity Bits IE: P-1, P-2, P-4...\nAs we know,\n\tP-1 Corresponds to D-3,D-5,D-7\n\tSimilarly,\n\t\tP-2 to D-3,D-6,D-7 And P-4 to D-5,D-6,D-7\n");
		printf("So,\n");
		printf("\tFor P-1 => D-3 D-5 D-7: %d %d %d\n",data[3],data[2],data[0]);
		condition = ((data[3]+data[2]+data[0])%2!=0)?1:0;
		if(condition)
			strcpy(Type0,"Odd");
		else
			strcpy(Type0,"Even");
		parity[2] = (type!=condition)?1:0;
		printf("\t\tSince we are using %s Parity and we have %s ones('1') in corresponding data bits, Parity = %d\n",Type,Type0,parity[2]);
		printf("\tFor P-2 => D-3 D-6 D-7: %d %d %d\n",data[3],data[1],data[0]);
		condition = ((data[3]+data[1]+data[0])%2!=0)?1:0;
		if(condition)
			strcpy(Type0,"Odd");
		else
			strcpy(Type0,"Even");
		parity[1] = (type!=condition)?1:0;
		printf("\t\tSince we are using %s Parity and we have %s ones('1') in corresponding data bits, Parity = %d\n",Type,Type0,parity[1]);
		printf("\tFor P-4 => D-5 D-6 D-7: %d %d %d\n",data[2],data[1],data[0]);
		condition = ((data[2]+data[1]+data[0])%2!=0)?1:0;
		if(condition)
			strcpy(Type0,"Odd");
		else
			strcpy(Type0,"Even");
		parity[0] = (type!=condition)?1:0;
		printf("\t\tSince we are using %s Parity and we have %s ones('1') in corresponding data bits, Parity = %d\n\n",Type,Type0,parity[0]);
		printf("Now,\n\tAs we have the complete list of Parity bits, Representing it in proper form, we get:\n");
		printHamming(data,parity,7);
	}
}
