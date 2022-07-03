/* 1. unsigned char: done
2. class: initiated with a parameterized constructor and calling two objects: one with parameterized constructor and other with default
3. obj1.func1().func2().func3()
4. 
*/

#include<iostream>
using namespace std;

class A{
    private:
    int c, d;
    public:
    A(int a, int b){
        cout<<a<<" "<<b;
    }
    int func1(int a, int b){
        c = a;
        d = b;
        cout<<c<<" "<<d;
    }
};

int main(){
    A a1(4, 6);
    A a2;
    a2.func1(4, 6);
    
    return 0;
}