#include<stdio.h>
/* defining ordinary differential equation to be solved */
/* in this example we are solving dy/dx = x+y */
#define f(x,y) x+y
void main(){
	float x0,y0,xn,h,yn,slope;
	int i,n;

	printf("Enter initial condition:\n");
	printf("\tx0 = ");
	scanf("%f",&x0);
	printf("\ty0 = ");
	scanf("%f",&y0);
	printf("Enter calculation point xn: ");
	scanf("%f",&xn);
	printf("Enter number of steps n: ");
	scanf("%d",&n);

	/* Calculation step size */
	h = (xn-x0)/n;

	/* Euler's method */
	printf("\n\tx0\ty0\tslope\tyn\n");
	printf("-----------------------------------------------\n");
	for(i=0;i < n;i++){
		slope = f(x0,y0);
		yn = y0 + h * slope;
		printf("\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n",x0,y0,slope,yn);
		y0 = yn;
		x0 = x0 + h;
	}

	/* Displaying result */
	printf("\n\n\t\tValue of y at x = %0.2f is %0.3f\n\n",xn,yn);

	return;
}
