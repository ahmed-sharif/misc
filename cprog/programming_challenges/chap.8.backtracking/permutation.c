#include <stdio.h>
int is_a_solution(int k, int n)
{
	// printf("is_a_solution %d %d\n", k, n);
	if(k==n-1)
		return 1;
	else
		return 0;
}

void process_solution(int a[], int k)
{
	int i;
	printf("{");
	for(i=1; i<=k; i++)
	{
		printf("%d ", a[i]);
	}
	printf("}\n");
}

void construct_candidates(int a[], int k, int n, int c[], int *ncandidates, int items[])
{
    int i; /* counter */
    int in_perm[5]; /* who is in the permutation? */
    for (i=0; i<5; i++) 
        in_perm[i] = 0;
    
    for (i=0; i<k-1; i++) 
        in_perm[ a[i] ] = 1;

    *ncandidates = 0;
    for (i=0; i<n; i++)
    {
        if (in_perm[i] == 0)
        {
            c[ *ncandidates] = i;
            *ncandidates = *ncandidates + 1;
        }
    }
    if(*ncandidates > 0)
    	printf("candidates\n");
    for(i=0; i<*ncandidates; i++)
    	printf("%d ", c[i]);
    if(*ncandidates > 0)
    	printf("\n");
}


void backtrack(int a[], int k, int n, int items[])
{
	int total_candidates, i;
	int candidates[20];
	// printf("%d %d\n", k, n);

	if(is_a_solution(k, n))
    {
		process_solution(a, k);
	}
	else
	{
		k = k + 1;
		construct_candidates(a, k, n, candidates, &total_candidates, items);
		for(i=0; i<total_candidates; i++)
		{
			a[k] = candidates[i];
			backtrack(a, k, n, items);
		}
	}
}

int main()
{
	int a[5];
	int items[5] = {10,20,30,40,50};
	int n = 5;
	int k = 0;
	// backtrack(a, k, n);
	backtrack(a, 0, 5,items);
	return 0;
}
