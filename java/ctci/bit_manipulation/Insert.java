public class Insert {

    public static void insert(int N, int M, int i, int j)
    {
        // N = 1024 , N = 10000000000
        // N = 19     M = 10011
        int x = 1 << (j - i + 1); // x = 100000
        x -= 1; // x = 011111
        x = x << i; // x = 000001111100
        x = ~ x;    // x = 111110000011
        N = N & x;  // clear bits from j to i in N
        M = M << i;
        N = N | M;
        System.out.println(N);
    }  
         
    public static void main(String [] args)
    {
        insert(1024, 19, 2, 6);
    }

}

