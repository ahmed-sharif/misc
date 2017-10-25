#include <stdio.h>


char arr[6] = {' ', 'a', 'b', 'c', 'd', 'e'};

int is_a_solution(int k, int n)
{
	if(k==n)
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
		if(a[i] == 1)
		{
			printf("%c ", arr[i]);
		}
	}
	printf("}\n");
	
}

void construct_candidate(int candidates[], int *total_candidates)
{
	*total_candidates = 2;
	candidates[0] = 1;
	candidates[1]= 0;
}

void backtrack(int a[], int k, int n)
{
	int total_candidates, i;
	int candidates[20];

	if(is_a_solution(k, n))
    {
		process_solution(a, k);
	}
	else
	{
		k = k + 1;
		construct_candidate(candidates, &total_candidates);
		for(i=0; i<total_candidates; i++)
		{
			a[k] = candidates[i];
			backtrack(a, k, n);
		}
	}
}

int main()
{
	int a[20];
	int n = 5;
	int k = 0;
	backtrack(a, k, n);
	return 0;
}
