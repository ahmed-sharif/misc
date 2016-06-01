#include <stdio.h>


int find_densest(int m[][2000], int w_nrows, int w_ncols, int row, int col)
{


  //n_array = array(m)
  //final_sums = arange((row - w_nrows + 1) * (col - w_ncols + 1))
  //print (row - w_nrows + 1) * (col - w_ncols + 1)
  int current = 0;
  int summ, max;
  int all_sums[20];
  int i, j, k, z;
  for(i=0; i<=row - w_nrows; i++)
  {
    
    // for i in range(row - w_nrows + 1):
    for(j=0; j <= col - w_ncols; j++)
    {

    
      // for j in range(col - w_ncols + 1):
      summ = 0;
      //  print ((row - w_nrows + 1) * (i)) + j + 1
      //  sliced_array = n_array[i:i+w_nrows, j:j+w_ncols]
      //# print sliced_array
      // for z in range(w_nrows):
      for(z=0; z<w_nrows; z++)
      {  
        //# print m[i+z][j:j+w_ncols]
        for(k=0; k<w_ncols; k++)
        {
            printf("%d ", m[i+z][j+k]);
            summ += m[i+z][j+k];
        }
        printf("\n");
        // summ += sum(m[i + z][j:j + w_ncols])
      }  
      printf("----\n");
      //# print summ
      all_sums[current++] = summ;
      // summs.append(summ)  
      // final_sums[current] = numpy_sum(sliced_array)
      //current += 1
      //# print
    }
  }
  //print len(summs)
  //print numpy_max(final_sums)
  max = all_sums[0];
  for(i=1; i<current; i++)
  {
      if(all_sums[i] > max)
      {
          max = all_sums[i];
      }
  }
  return max;
}


int main()
{
    int test_cases, w_ncols, w_nrows, cols, rows;
    int i, j, k;
    int input[1900][2000];
    scanf("%d", &test_cases);

    while(test_cases > 0)
    {
        printf("Processing case %d\n", test_cases);
        scanf("%d %d",&w_nrows, &w_ncols);
        scanf("%d %d",&rows, &cols);

        for(i=0; i<rows; i++)
            for(j=0; j<cols; j++)
                scanf("%d", &input[i][j]);
        printf("calling %d\n", test_cases);      
        printf("%d\n", find_densest(input, w_nrows, w_ncols, rows, cols));
        test_cases--;      
    }
    
    return 0;  
}