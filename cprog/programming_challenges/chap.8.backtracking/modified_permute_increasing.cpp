#include "stdio.h"

#define NMAX 1000
#define MAXCANDIDATES 1000


int found_solution = 0;

/* char original_items[4] = {'h', 'e', 'f', 'g'}; */
char original_items[4] = {'d', 'k', 'h', 'c'};

void process_solution(int a[], int k, char items[])
{
    int i;              /* counter */
    
    printf("{");
    for (i=1; i<=k; i++)
        //printf(" %d", a[i]);
        printf(" %c", items[a[i]-1]);

    printf(" }\n");
}

bool is_a_solution(int a[], int k, int n)
{
    return (k == n);
}
/*
int compare_items(int a[], k)
{
    int i;
    int x=0;
    
    for(i=1; i<=k; i++)
    {
        original_items[]  original_items[a[i]] >=
    }
}
*/
int is_valid_position(int a[], int i, int k)
{
    int length = 4;
    int ret_val = 0;
    int j, x, temp;
    int passed = 1;
    printf("Exising ##");
    
    for (x=0; x<k; x++)
    {
        printf("%d ",a[x]);
    }    
    printf("\n");
    
    temp = a[k];
    a[k] = i;
    
    for(j=1; j<=k; j++)
    {
        printf("compare %c with %c \n", original_items[a[j-1]], original_items[j-1]);
        if(original_items[a[j-1]] >= original_items[j-1])
        {
            printf("pass\n");
        }
        else
        {
            printf("not pass break\n");
            passed = 0;
            break;
        }
    }

    a[k] = temp;
    
    printf("choosing %c for position %d\n", original_items[i],k);
    
    if (passed)
    {
        printf("passed\n");
    }
    else
    {
        printf("not passed\n");

    }

    return passed;

    if (original_items[k-1] > original_items[i] && k != length)
    {
        printf("\tbad choice\n");
        ret_val = 0;
    }
    else
    {
        printf("\tgoodd choice\n");
        ret_val = 1;
    }
    
    return ret_val;
}


/*  What are possible elements of the next slot in the permutation?  */

void construct_candidates(int a[], int k, int n, int c[], int *ncandidates)
{
    int i;              /* counter */
    bool in_perm[NMAX];     /* what is now in the permutation? */

    for (i=1; i<NMAX; i++) in_perm[i] = false;
    for (i=1; i<k; i++) in_perm[ a[i] ] = true;

    *ncandidates = 0;
    for (i=1; i<=n; i++) 
        if (in_perm[i] == false) {
            if(is_valid_position(a, i-1, k))
            {
                c[ *ncandidates] = i;
                *ncandidates = *ncandidates + 1;
            }
        }
}

int is_same_as_original(int a[], int k)
{
    int i;
    int same = 1;
    for(i=1; i<=k; i++)
    {
        if (a[i] != i)
        {
            same = 0;
            break;
        }
    }
    /* printf("\n"); */
    return same;
}

void backtrack(int a[], int k, int n,char items[])
{
        int c[MAXCANDIDATES];           /* candidates for next position */
        int ncandidates;                /* next position candidate count */
        int i;                          /* counter */

        if(found_solution)
            return;


        if (is_a_solution(a, k, n))
        {   
                if (! is_same_as_original(a, k))
                {
                    process_solution(a, k, items);
                    found_solution = 1;
                }
        }
        else {
                k = k+1;
                construct_candidates(a, k, n, c, &ncandidates);
                for (i=0; i<ncandidates; i++) {
                        a[k] = c[i];
                        backtrack(a, k, n,items);
                }
        }
}

int main()
{
    // char items[5] = {'a','b','c','d','e'};
    int a[NMAX];            /* solution vector */
    // char items[4] = {'h', 'e', 'f', 'g'};
    // backtrack(a,0,4,items);

    char items1[4] = {'d', 'k', 'h', 'c'};
    backtrack(a,0,4,items1);
    return 0;
}

