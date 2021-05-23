#include <stdio.h>
#include <math.h>
void main(){
	int i,n,m,sum=0,h;
	printf("Enter the size of disc:");
	scanf("%d",&m);
	printf("Enter number of requests:");
	scanf("%d",&n);
	printf("Enter the requests:\n");
	//creating array of size n
	int a[20];
	for (i = 0; i < n; ++i){
		scanf("%d",&a[i]);
		if(a[i]>m){
			printf("Error, inputed position is out of bound.\n");
			return;
		}
	}
	printf("Enter the head position: ");
	scanf("%d",&h);
	//head will be at h at the starting
	int temp=h;
	printf("%d", temp);
	for (i = 0; i < n; ++i){
		printf(" --> %d", a[i]);
		//the difference for the head movement
		sum+=abs(a[i]-temp);
		//head is now at new i/o request
		temp = a[i];
	}
	printf("\n");
	printf("Total head movements = %d\n", sum);
}