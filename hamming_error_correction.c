#include<stdio.h>
#include<string.h>
#include<math.h>

int verify(char data[8]){
	int i1=0,i0=0;
	if(strlen(data)!=7){
		printf("Invalid data length: %d",strlen(data));
		return 0;
	}
	else{
		for(int i=0;i<7;i++){
			if(data[i]=='1')
				i1++;
			else if(data[i]=='0')
				i0++;
		}
		if(i0+i1!=7){
			printf("Data contains invalid character.");
			return 0;
		}
		else
			return 1;
	}
}
void printHamming(int data[8]){
	printf("\t\t\t.............................\n");
	printf("\t\t\t| %d | %d | %d | %d | %d | %d | %d |\n",data[0],data[1],data[2],data[3],data[4],data[5],data[6]);
	printf("\t\t\t'---------------------------'\n");
	printf("\t\t          ^   ^   ^   ^   ^   ^   ^\n");
	printf("\t\t\t D-7 D-6 D-5 P-4 D-3 P-2 P-1\n");
}
int toInt(int error[4]){
	int num=0,dec=0,rem,i=2;
	for(;i>=0;i--)
		num += error[i] * pow(10,2-i);
	i = 0;
	while(num!=0){
		rem = num%10;
		num /= 10;
		dec += rem * pow(2,i);
		++i;
	}
	return dec;
}
void main(){
	char tempData[8],Type[5],Type0[5];
	int data[8],error[4],type,condition,err;
	printf("Input the 7 bit data from receiver: ");
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
		for(int i=0;i<7;i++)
			if(tempData[i]=='1')
				data[i] = 1;
			else
				data[i] = 0;
		printf("\n\n==========> Hamming code Using %s Parity System on Data: %d%d%d%d%d%d%d <=========",Type,data[0],data[1],data[2],data[3],data[4],data[5],data[6]);
		printf("\nRepresenting given data into hamming code format:\n");
		printHamming(data);
		printf("Firstly,\n\tTo know error position, we need to find error bits IE: E-4,E-2,E-1 with help of parity bits.\nAs we know,\n\tP-1 Corresponds to D-3,D-5,D-7\n\tSimilarly,\n\t\tP-2 to D-3,D-6,D-7 And P-4 to D-5,D-6,D-7\n");
		printf("So,\n");
		printf("\tP-1 D-3 D-5 D-7 => %d %d %d %d\n",data[6],data[4],data[2],data[0]);
		condition = ((data[6]+data[4]+data[2]+data[0])%2!=0)?1:0;
		if(condition)
			strcpy(Type0,"Odd");
		else
			strcpy(Type0,"Even");
		error[2] = (type!=condition)?1:0;
		printf("\t\tSince we are using %s Parity and we have %s ones('1') in corresponding data including parity, Error = %d\n",Type,Type0,error[2]);
		printf("\tP-2 D-3 D-6 D-7 => %d %d %d %d\n",data[5],data[4],data[1],data[0]);
		condition = ((data[5]+data[4]+data[1]+data[0])%2!=0)?1:0;
		if(condition)
			strcpy(Type0,"Odd");
		else
			strcpy(Type0,"Even");
		error[1] = (type!=condition)?1:0;
		printf("\t\tSince we are using %s Parity and we have %s ones('1') in corresponding data including parity, Error = %d\n",Type,Type0,error[1]);
		printf("\tP-4 D-5 D-6 D-7 => %d %d %d %d\n",data[3],data[2],data[1],data[0]);
		condition = ((data[3]+data[2]+data[1]+data[0])%2!=0)?1:0;
		if(condition)
			strcpy(Type0,"Odd");
		else
			strcpy(Type0,"Even");
		error[0] = (type!=condition)?1:0;
		printf("\t\tSince we are using %s Parity and we have %s ones('1') in corresponding data including parity, Error = %d\n",Type,Type0,error[0]);
		printf("Now,\n\tAs we have the complete list of Error bits IE:%d%d%d\n", error[0],error[1],error[2]);
		err = toInt(error);
		printf("\tRepresenting it in decimal form, we get error position: %d\n",err);
		if (err!=0){
			printf("Finally,\n\tAfter changing value at the error position, we get the correct data from the sender as:\n");
			err = 7-err;
			data[err] = (data[err] == 1)?0:1;
		}
		else
			printf("Finally,\n\tAs we have found above, We can say the data received at receiver have no Error and needs no correction\n\t IE: Correct bits:\n");
		printHamming(data);
	}
}
