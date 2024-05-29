// declaring_lambda_expressions2.cpp
#include <functional>
#include <iostream>

int main()
{
   using namespace std;
   int i = 3, j = 5;

   // The following lambda expression captures i by value and j by reference.
   function<int (void)> f = [i, &j] {
       cout<<"\nInside lambda expression, i is: "<<i<<" j is: "<<j<<endl;
       return i + j; };
   // Change the values of i and j.
   i = 22, j = 44;
   cout<<"\ni is: "<<i<<" j is: "<<j<<endl;

   // Call f and print its result.
   cout <<"\nLambda expression value is: " <<f() << endl;
   cout<<"\ni is: "<<i<<" j is: "<<j;
   
   auto fLambda = [&i, j](int m, float k){cout<<"\nfLamda executed";
        for(int p=0; p<m; p++) cout<<" "<<(i+j)*p+k;
        return i+j;}(5, 1.1); // [](){}
        
   cout<<"\n"<<fLambda;
   //cout<<"\n"<<fLambda(3, 2.5);
   return 0;
}