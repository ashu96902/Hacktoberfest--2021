import java.util.*;
class q1
{
    public static void main(String args[])
    {
        Scanner d= new Scanner(System.in);
        int n=d.nextInt();
        int a[]=new int[n];
        int i;
        for(i=0;i<n;i++)
        {
            a[i]=d.nextInt();
        }
        System.out.println(sum1(a));
    }

    static int sum1(int a[])
    {
        int l=a.length;
        int i,j;
        int s=0;
        Arrays.sort(a);
        for(i=0;i<l;i++)
        {
            s+=a[i]*(l-i);
        }
        return s;
    }

    static int sum2(int a[])
    {
        int l=a.length;
        int i,j;
        int s=0;
        int ps[]=new int[l];
        ps[0]=a[0];
        for(i=1;i<l;i++)
        {
            if(a[i]<ps[i-1])
                ps[i]=a[i];
            else
                ps[i]=ps[i-1];
        }
        for(i=0;i<l;i++)
        {
            s+=ps[i]*i;
        }
        for(i=0;i<l;i++)
        {
            s+=a[i];
        }
        return s;
    }
}
