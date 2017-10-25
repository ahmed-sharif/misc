
public class Permutation
{
    public static void permutation(String str) 
    {
        permutation(str, "");
    }

    public static void permutation(String str, String prefix, int tabs) 
    {
        System.out.println("permutation(str=\""+str+"\""+", prefix=\""+prefix+"\")");
        if (str.length() == 0) 
        {
            System.out.println(prefix);
        } 
        else 
        {
            for (int i= 0; i < str.length(); i++) 
            {

                String rem = str.substring(0, i) + str.substring(i + 1);
                System.out.println("rem="+rem);
                permutation(rem, prefix + str.charAt(i));
            }
        }
    }

    public static void main(String args[])
    { 
        String inp = "1234";
        permutation(inp);

    }

}


