#include <iostream>
int i;

class Parent {
public:
    Parent(){
        ++i;
        std::cout<<"Parent "<<i <<std::endl;
    }
    //virtual void say() {
    void say() {
        std::cout << "\nParent said.";
    }
};

class Child1 : public Parent {
public:
    void say()
    {
        std::cout << "\nChild 1";
    }
};

class Child2 : public Parent {
public:
    void say()
    {
        std::cout << "\nChild 2";
    }
};

class Child3 : public Parent {
public:
    void say()
    {
        std::cout << "\nChild 3";
    }
};

int main()
{
    Parent* parents[3]; // Parent Constructor called at the time of creation of parents objects.
    parents[0] = new Child1();
    parents[1] = new Child2();
    parents[2] = new Child3();

    for (int i=0; i<3; ++i)
        parents[i]->say();

    return 0;
}

/* This is the classic question of how polymorphism works I think.
The main idea is that you want to abstract the specific type for each object.
In other words: You want to be able to call the Child instances without knowing it's a child!

Here is an example: Assuming you have class "Child1" and class "Child2" and "Child3" you want to
be able to refer to them through their base class (Parent).

As you can imagine, this is very powerful. It lets you extend the Parent as many times as you want
and functions that take a Parent pointer will still work. For this to work as others mention
you need to declare the method as virtual.
*/
