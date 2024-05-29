#include<iostream>
//#include<bits/stdc++.h>
using namespace std;

// C++ implementation of right rotationof an array K number of times Function to rightRotate array
void RightRotate(int a[], int n, int k)
{
	// If rotation is greater than size of array
	k = k % n;

	for(int i = 0; i < n; i++)
	{
	if(i < k) //Suppose n=10 and k=3. for i=0,1 if condition will hit.
		cout << a[n + i - k] << " "; // Printing rightmost kth elements
	else
		cout << (a[i - k]) << " "; // Prints array after 'k' elements
	}
	cout << "\n";
}

int main() {
int a = 5, c;
int *ptr = &a;
cout<<"\nThe address of a is: "<< ptr;
c = *ptr;
cout<<"\nThe value at the address of "<<ptr<<" is: "<<c<<" or "<<*ptr;

	int Array[] = { 1, 2, 3, 4, 5 };
	int N = sizeof(Array) / sizeof(Array[0]);
	int K = 2;
	cout<<"\nThe rotate value of the array "<< Array[3]<<" is: ";
	RightRotate(Array, N, K);
}
