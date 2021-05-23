#include <stdio.h>
float calculate_tax(float amt){
	// range of tax for tax rate, Upper boundry value
	// example {400000,500000,700000,1300000} for 0-400000,400001-500000,500001-700000,700001-1300000,1300001-above
	float range[] = {400000,500000,700000,1300000};
	// rate of tax for tax range defined above, start from 0-
	// example {0,10,20,30,36} for 0-400000=>0%,400001-500000=>10%,500001-700000=>20%,700001-1300000=>30%,1300001-above=>36%
	float rate[] = {0,10,20,30,36};
	// number of items in rate
	// length of {0%,10%,20%,30%,36%} = 5
	int l = 5;

	//don't modify anything below it
	float diff[l];
	for (int i = 0; i < l; ++i)
		if (i == 0)
			diff[0] = range[0]-0.0;
		else if (i == l-1)
			diff[i] = amt;
		else
			diff[i] = range[i]-range[i-1];
	float tax = 0.0;
	for (int i = 0; i < l; ++i)
		if (amt <= diff[i]){
			tax += amt * rate[i]/100;
			break;
		}
		else{
			amt -= diff[i];
			tax += diff[i] * rate[i]/100;
		}
	return tax;
}


void main(int argc, char const *argv[]){
	float amount;
	printf("Amount: ");
	scanf("%f", &amount);
	printf("%0.2f ==> %0.2f\n", amount, calculate_tax(amount));
}