#include <stdio.h>
void main(){
	int i,j,n,page[50],frameno,frame[10],move=0,flag,count=0;
	float rate;
	printf("Enter the number of pages: ");
	scanf("%d",&n);
	printf("Enter the page reference numbers:\n");
	for (i = 0; i < n; ++i)
		scanf("%d",&page[i]);
	printf("Enter the number of frames: ");
	scanf("%d",&frameno);
	for (i = 0; i < frameno; ++i)
		frame[i] = -1;
	printf("Page reference string \t Frames\n");
	printf("--------------------------------------------------------\n");
	for (i = 0; i < n; ++i){
		printf("%d\t\t\t", page[i]);
		flag=0;
		for(j=0;j<frameno;j++){
			if(page[i] == frame[j]){
				flag = 1;
				printf("No replacement\n");
				break;
			}
		}
		if(flag==0){
			frame[move]=page[i];
			move = (move+1)%frameno;
			count++;
			for (j = 0; j < frameno; ++j)
				printf("%d\t", frame[j]);
			printf("\n");
		}
	}
	rate = (float) count/(float)n;
	printf("Number of page faults is %d.\n", count);
	printf("Fault rate is %f.\n", rate);
}