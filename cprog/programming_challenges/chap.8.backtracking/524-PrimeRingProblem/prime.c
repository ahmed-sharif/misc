
int in_primes(int number)
{
    int primes[10] = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
    int i;
    int count = 10;
    for (i = 0; i < count; i++)
    {
        if(primes[i] == number)
        {
            return 1;
        }
    }
    return 0;
}

void construct_candidates(int a[], int k, int n, int *ncandidates, int all_candidates[])
{
    int in_perms[17], i; 
    if (k == 1)
    {
        *ncandidates = 1;
        all_candidates[0] = 1;
    }

    else
    {
        for (i = 0; i < 17; i++)
            in_perms[i] = 0;

        for(i =1; i<k; i++)
            in_perms[a[i]] = 1;
            

        candidates = []
        *ncandidates = 0;
        for (i=2; i < n + 1; i++)
        {
            if(! in_perms[i])
            {
                if (n != k)
                {
                    if (in_primes(a[k-2] + i))
                    {
                        all_candidates[*ncandidates] = i;
                        *ncandidates = *ncandidates + 1;
                    }
                }
                else
                {
                    if(in_primes(a[0] + i) && in_primes(a[k-2] + i))
                    {
                        all_candidates[*ncandidates] = i;
                        *ncandidates = *ncandidates + 1;    
                    }
                }
            }

        }
    }
}
    

void print_result(int a[], int n)
{
    int i;
    printf("%d", a[0]);
    for(i = 1; i < n; i++)
    {
        printf(" %d", a[i]);
    }
    printf("\n");
}

void backtrack(int a[], int k, int n)
{
    int all_candidates[17];
    int ncandidates, i;

    if (n == k)
    {
        print_result(a, n);
    }
    else
    {
        k = k + 1;
        candidates = construct_candidates(a, k, n, &ncandidates, all_candidates);
        # print k, candidates, a
        for can in candidates:
            a[k-1] = can
            backtrack(a, k, n)
            a[k-1] = 0
    }
}

    

#n = 6
#a = [0 for _ in range(n)]
#backtrack(a, 0, n)

n = 8
a = [0 for _ in range(n)]
backtrack(a, 0, n)



int main()
{

    int n, k;
    
    while(scanf("%d",&n)!=EOF)
    {
        orglow=low;
        orghigh=high;
        if(low > high)
        {
            temp=low;
            low=high;
            high=temp;
        }
        
        maxlength=0;
        for(i=low;i<=high;i++)
        {
            length=getlength(i);
            if(length > maxlength)
            {
                maxlength=length;
            }
            //printf("length %d=%d\n",i,length);
        }
        printf("%d %d %d\n",orglow,orghigh,maxlength);
    }
    

    return 0;   
}
