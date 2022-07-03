#include <iostream>
#include<conio.h>
using namespace std;
void main()
{
   int k = 3, n = 4;
   int Stdnt_Cr_limit = {40, 50, 30, 80}, Subs_cr = {20, 30, 25}, Sub_cr = sorted(Subs_cr);
    cout<<Sub_cr;

    int count = 0, total_count = 0, total = 0;

    for (i =0, i<=n, i++)
    {
        int p = 0, Cr_sub = 0;
        print("\n\nFor the {}th student: ".format(i+1));

        for (j =p, i<=k, j++)
        {
            print("\n{}th subject credit is: ".format(j+1) , Sub_cr[j]);

            if (Cr_sub + Sub_cr[j]) <= Stdnt_Cr_limit[i]:
            {
                print("Previous count: ", count)
                count+= 1
                print("Count: ", count)

            }
            
            
        print("Subjects counts: ", count)
            
        Cr_sub+= Sub_cr[p]
        p+= 1
    
        print("Subjects credit added: ", Cr_sub)

        }
        
    total_count += count
    total += 1
    print("Total count for the {}th student".format(i+1), total_count, "\t", total)

    }
   
        
print("\n\nNumber of ordered pairs are: ", count, total_count)
print("Total number of subject are: ", p, " and the total credits of the subjects is: ", Cr_sub)
}