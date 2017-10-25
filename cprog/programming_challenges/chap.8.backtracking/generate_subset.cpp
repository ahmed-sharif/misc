

#include <stdio.h>

bool finished = false; /* found all solutions yet? */

bool is_a_solution(int a[], int k, int n)
{
    return (k == n); /* is k == n? */
}

void process_solution(int a[], int k, int indent)
{
    int i; /* counter */
    for (i=0; i<indent; i++)
    {
        printf("\t");
    }
    printf("{");
    for (i=1; i<=k; i++)
    {
        // if (a[i] == true)
        if (a[i] == 1)
        {
            printf(" %d",i);
        } 
    }
    printf(" }\n");
}

void construct_candidates(int a[], int k, int n, int c[], int *ncandidates)
{
    c[0] = 1;
    c[1] = 0;
    *ncandidates = 2;
}

void backtrack(int a[], int k, int input, int indent)
{
    int c[20]; /* candidates for next position */
    int ncandidates; /* next position candidate count */
    int i; /* counter */
    for (i=0; i<indent; i++)
    {
        printf("\t");
    }
    for(i=1; i<=k;i++)
        printf("%d ", a[i]);

    printf("k=%d, indent=%d\n",k, indent);

    if (is_a_solution(a,k,input))
    {
        process_solution(a,k, indent);
    }
    else 
    {
        k = k+1;
        construct_candidates(a,k,input,c,&ncandidates);
        for (i=0; i<ncandidates; i++) 
        {
            a[k] = c[i];
            backtrack(a,k,input, indent+1);
            if (finished) 
                return; /* terminate early */
        }
    }
}

void generate_subsets(int n)
{
    int a[20]; /* solution vector */
    int k = 0;
    backtrack(a, k, n, 0);
}

int main()
{
    generate_subsets(3);
}