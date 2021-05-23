#include<stdio.h>
#include<stdlib.h>
#include<math.h>

/*
 * Defining equation to be solved.
 * Change this equation to solve another problems.
 */
#define f(x) 44*x*x*x + 5280*x*x - 56847;

/*
 * Defining derivatives of g(x).
 * As you change f(x), change this function also.
 */
#define g(x) 132*x*x + 10560*x;

void main(){
    float x0,x1,f0,f1,g0,e;
    int step = 1,N;
    
    /* Inputs */
    printf("\nEnter initial guess: ");
    scanf("%f",&x0);
    printf("\nEnter error tolerence: ");
    scanf("%f",&e);
    printf("\nEnter max iteration: ");
    scanf("%f",&N);
    
    /* Implementing Newton Raphson Method */
    printf("\n\tStep\t\tx0\t\tf(x0)\t\tx1\t\tf(x1)\n");
    printf("---------------------------------------------------------------------------------------------\n");
    do{
        g0 = g(x0);
        f0 = f(x0);
        if(g0 == 0.0){
            printf("Mathemetical Error.\n");
            exit(0);
        }
        x1 = x0 - f0/g0;
        printf("\t%d\t\t%f\t\t%f\t\t%f\t\t%f\n",step,x0,f0,x1,f1);
        x0 = x1;
        step = step+1;
        if(step > N){
            printf("Not Convergent.\n");
//             exit(0);
            break;
        }
        f1 = f(x1);
    }while(fabs(f1) > e);
    
    /* Print root */
    printf("\n\t\tRoot = %f",x1);
}
