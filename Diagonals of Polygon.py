import java.util.Scanner;
public class java{
    public static void main(String args[])
    {
        int n;
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        int k=n*(n-3)/2;
        System.out.println(k);
    }
}