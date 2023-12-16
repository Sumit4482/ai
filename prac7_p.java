import java.util.*;
class prac7_p
{
    Scanner sc = new Scanner(System.in);
    char w [][] = new char[5][5];
    int np; // number of pits
    int wp,gp; //wumpus position number of golds
    int pos[]; // position of pits
    int b_pos[]= new int[20]; // position of breeze
    int s_pos[] = new int[20]; // position of stench

    void accept(String w[][])
    {
        for(int i=0;i<20;i++)
        {
            b_pos[i] = -1;
            s_pos[i] = -1;

        }

        for(int i=0;i<5;i++)
        {
            for(int j=0;j<5;j++)
            {
                w[i][j] ="";
            }
        }

        int count = 1;
        System.out.println("\n\n********* Wumpus World Problem *********\n\n");

        System.out.println("The positions are as follows: \n");

        for(int i=1;i<=4;i++)
        {
            System.out.println("\n--------------------------------------------");
            System.out.print("\t|");
            for(int j=1;j<=4;j++)
            {
                System.out.print(count+"\t|\t");
                count++;
            }
        }
        System.out.println("\n--------------------------------------------");
        System.out.println("\n Agent start position: 13");
        w[4][1] = "A";
        System.out.println("\n Enter the number of pits: ");
        np = sc.nextInt();
        pos = new int[np];
        System.out.println("Positions of pits,gold and wumpus should not overlap");
        System.out.println("\n Enter the position of pits: ");
        for(int i=0;i<np;i++)
        {
            pos[i] = sc.nextInt();
            show_sense(pos[i],1,w);

        }
        System.out.println("\n Enter the position of wumpus: ");
        wp = sc.nextInt();
        show_sense(wp,2,w);
        System.out.println("\n Enter the position of gold: ");
        gp = sc.nextInt();

        insert(w);
    }

    void insert(String w[][])
    {
        int temp=0;
        int count = 0;
        int flag1 = 0,flag2 = 0;
        for(int i=0;i<np;i++)
        {
            temp = pos[i];
            count = 0;
            for(j=0;j<=4;j++)
            {
                for(int k=0;k<=4;k++)
                {
                    ++count;
                    if(count == temp)
                    {
                        w[j][k] += "P";
                       
                    }
                    else if(count==gp && flag1==0)
                    {
                        w[j][k] += "G";
                        flag1 = 1;
                    }
                    else if(count==wp && flag2==0)
                    {
                        w[j][k] += "W";
                        flag2 = 1;
                    }
                    
                }
                
            }
        }
        display(w);
    }

    void show_sense(int a,int b, String w[][])
    {
        int t1,t2,t3,t4;
        t1 = a-1;
        t2 = a+1;
        t3 = a-4;
        t4 = a+4;
        if(a==5||a==9)
        {
            t1=0;
        }
        if(a==8||a==12)
        {
            t2=0;
        }
        if(a==4)
        {
            t2=0;
        }
        if(a==13)
        {
            t1=0;
        }
    }



}