// constructors and derived classes
#include <iostream>
using namespace std;

class Mother {
  public:
    Mother () //Constructor 1 without any parameters.
      { cout << "Mother: no parameters\n"; }
    Mother (int a) //Constructor 2 with an int parameter.
      { cout << "Mother: int parameter\n"; }
};

class Daughter : public Mother {
  public:
    Daughter (int a) // It will 1st invoke the Consturctor 1 of the Base Class.
      { cout << "Daughter: int parameter\n\n"; }
};

class Son : public Mother {
  public:
    Son (int a) : Mother (a) // It will 1st invoke Constructor 2 of the Base Class.
      { cout << "Son: int parameter\n\n"; }
};

int main () {
  Daughter kelly(0); //It will invoke the Base Class Constructor (with no paramter) follwed by the Dervied Class Constructor.
  Son bud(0); //It will invoke the Base Class Constructor (with int parameter) follwed by the Dervied Class Constructor.
  
  return 0;
}