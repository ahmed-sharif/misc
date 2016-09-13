/* Book: programming challenges */
#include <stdio.h>


void printmat(int mat[10][10], int n)
{
	int i, j;
	for(i=0;i<=n;i++)
        {
		for(j=0;j<=n;j++)
                {
			printf("%2d ",mat[i][j]);
                }
		printf("\n");
        }
	printf("--------------\n");
}

int binomial_coefficient(int n, int m) 
{
	int i,j; /* counters */
	int bc[10][10]; /* table of binomial coefficients */
	for (i=0; i<=n; i++) 
		bc[i][0] = 1;
	printmat(bc, n);


	for (j=0; j<=n; j++) 
		bc[j][j] = 1;
	printmat(bc, n);


	for (i=1; i<=n; i++)
        {
		for (j=1; j<i; j++)
                {
			bc[i][j] = bc[i-1][j-1] + bc[i-1][j];
			printmat(bc, n);
                }
        }
	return( bc[n][m] );
}


int main()
{
	binomial_coefficient(6, 4);
	return 0;	
}
