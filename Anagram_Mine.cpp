// C++ program to sort a string of characters
#include<bits/stdc++.h>
using namespace std;

// function to print string in sorted order
void sortString(string &str)
{
sort(str.begin(), str.end());
cout << str;
}

// Driver program to test above function
int main()
{
	string s = "geeksforgeeks";
	sortString(s);
	return 0;
}

    char str1[20], str2[20];
    int len1, len2, i, j, found=0, not_found=0;
    cout<<"Enter the First String: ";
    cin>>str1;
    cout<<"Enter the Second String: ";
    cin>>str2;