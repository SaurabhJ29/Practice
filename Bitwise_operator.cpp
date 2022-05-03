#include <iostream>
using namespace std;

int main() {

	// a = 5(00000101), b = 9(00001001)
    unsigned char c1 = 1, c2 = 2; 
  
    // The result is 00001010 
    cout <<"a<<1 = "<< (c1<<1) << endl;

    cout <<"1<<2 = "<< (1<<2) << endl;
    
    // The result is 00010010 
    cout <<"b<<1 = "<< (c2<<1) << endl;
    cout <<"1>>2 = "<< (1>>2) << endl;


	// a = 5(00000101), b = 9(00001001)
	int a = 5, b = 9;

	// The result is 00000001
	cout<<"a = " << a <<","<< " b = " << b <<endl;
	cout << "a & b = " << (a & b) << endl;

	// The result is 00001101
	cout << "a | b = " << (a | b) << endl;

	// The result is 00001100
	cout << "a ^ b = " << (a ^ b) << endl;

	// The result is 11111010
	cout << "~(" << a << ") = " << (~a) << endl;

	// The result is 00010010
	cout<<"b << 1" <<" = "<< (b << 1) <<endl;   // result is 18

	// The result is 00000100
	cout<<"b >> 1 "<<"= " << (b >> 1 )<<endl;  // result is 4

	return 0;
}

// This code is contributed by sathiyamoorthics19
