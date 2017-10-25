#include <stdio.h>
#include <stdlib.h>



struct stack {
    int height;
    int index;
};

void print(struct stack s[], int n)
{
    int i = 0;
    for(i=0; i<n; i++)
    {
        printf("index = %d, item = %d\n", s[i].index, s[i].height);
    }
}

int max_area(int A[], int n)
{
    int i, mx_area = -1, top = -1, left, current_area;

    struct stack *S = (struct stack *)malloc(sizeof(struct stack) * n);

    for(i=0; i<=n; i++)
    {
        printf("current item %d\n", A[i]);
        while(top >= 0 && (i == n || S[top].height > A[i]))
        {
            if(top > 0)
            {
                left = S[top - 1].index;
            }
            else
            {
                left = -1;
            }
            printf("\tleft=%d\n", left);
            current_area = (i - left - 1) * S[top].height;
            printf("\tcurrent_area=(%d - %d - 1) * %d = %d\n", i, left, S[top].height, current_area);
            --top;
            if(current_area > mx_area)
            {
                mx_area = current_area;
            }
            printf("\tmax_area=%d, top=%d\n", mx_area, top);
            printf("\t-------------------\n");
        }

        if (i < n)
        {
            ++top;
            S[top].height = A[i];
            S[top].index = i;
            printf("pushing index=%d, height=%d to top=%d\n", i, A[i], top);
        }
    }
    return mx_area;
}


int main()
{
    int i;
    int arr[] = {3, 2, 5, 6, 3, 4, 4};
    for(i=0; i<7; i++)
        printf("%d ", arr[i]);
    printf("\n");
    printf("%d\n", max_area(arr, 7));
    return 0;
}
