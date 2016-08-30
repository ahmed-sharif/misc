public class RangeFind {

    static int binarySearchStart(int[] values, int start, int end, int value)
    {
       if(start > end)
       {
           return -1;
       }
       int mid = (start + end) / 2;
       if((value == values[mid]) && ((mid == 0) || (value > values[mid - 1])))
       {
          return mid;
       }
       else if(value > values[mid])
       {
          return binarySearchStart(values, mid + 1, end, value);
       }
       else
       {
          return binarySearchStart(values, start, mid - 1, value);
       }
    }
      
    static int binarySearchEnd(int[] values, int start, int end, int value)
    {
       if(start > end)
       {
           return -1;
       }
       int mid = (start + end) / 2;
       if((value == values[mid]) && ((mid == values.length - 1) || (value < values[mid + 1])))
       {
          return mid;
       }
       else if(value < values[mid])
       {
          return binarySearchEnd(values, start, mid - 1, value);
       }
       else
       {
          return binarySearchEnd(values, mid + 1, end, value);
       }
    }
         
    public static void main(String [] args)
    {
        int [] values = {0, 0, 0, 1, 2, 3, 3, 3, 3, 10, 10};
        int value = 3;
        int start = binarySearchStart(values, 0, values.length, value);
        int end   = binarySearchEnd(values, start, values.length, value);
        System.out.println(value+" is at ["+start+":"+end+"]");
    }

}

