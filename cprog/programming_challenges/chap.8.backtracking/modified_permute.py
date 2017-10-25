#include "stdio.h"

#define NMAX 1000
#define MAXCANDIDATES 1000

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
            c[ *ncandidates] = i;
            *ncandidates = *ncandidates + 1;
        }
}

void backtrack(int a[], int k, int n,char items[])
{
        int c[MAXCANDIDATES];           /* candidates for next position */
        int ncandidates;                /* next position candidate count */
        int i;                          /* counter */

        if (is_a_solution(a, k, n))
                 process_solution(a, k, items);
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
    char items[5] = {'a','b','c','d','e'};
    int a[NMAX];            /* solution vector */
    backtrack(a,0,3,items);
    return 0;
}


if __name__ == '__main__':
    main()
