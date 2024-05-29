// C++ Program of above approach
#include <iostream>
#include <math.h>
#include <cstring>
using namespace std;

class PowerSet
{
	
public:
void printPowerSet(char *set, int set_size)
{
	/*set_size of power set of a set with set_size n is (2**n -1)*/
	unsigned int pow_set_size = pow(2, set_size);
	int i, j;

	/*Run from counter 000..0 to 111..1*/
    cout<<"\nThe number of elements in Power Set are: "<<pow_set_size;
    cout<<"\n\nThe elements of Power set are: ";
	for(i = 0; i < pow_set_size; i++)
	{
	for(j = 0; j < set_size; j++)
	{
		/* Check if jth bit in the counter is set
			If set then print jth element from set */
		if(i & (1 << j))
			cout << set[j];
	}
	cout << "\t";
	}
} 
};

/*Driver code*/
int main()
{
	PowerSet g, h, s;
	char x = 'l', set[] = {'a','b','c'}, set1[] = {'s', 'a', 'u', 'r','a'}, set2[] = {'h','o','m', 'e'};
    cout<<"\nThe 1st element of set is: "<< set[0];
	cout<<"\nThe 2nd element of set is: "<< set[1];
	cout<<"\nThe 3rd element of set is: "<< set[2];
    cout<<"\nThe length of set is: "<< strlen(set);
	int a = 5;
	int* b = &a;
	cout<<"\nThe address of a and 4 is: "<<b;
    char* p = &set1[3];
	char* m = &set2[1];
	char* v = &x;
    cout<<"\nThe address of first element of the array char is: "<<p<<"\t"<<m<<"\t"<<v;
	g.printPowerSet(set, sizeof(set));
    // h.printPowerSet(set1, sizeof(set1));
    // s.printPowerSet(set2, sizeof(set2));
	return 0;
}
// This code is contributed by SoM15242
