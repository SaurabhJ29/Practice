// CPP program to demonstrate multithreading using three different callables.
#include <iostream>
#include <thread>
using namespace std;

void foo(int Z)		// A dummy function
{
	for (int i = 0; i < Z; i++) {
		cout << "\nThread using function pointer as callable: "<<i<<"\n";
	}
}

class thread_obj { 	// A callable object
public:
	void operator()(int x) // 
	{
		for (int i = 0; i < x; i++)
			cout << "\nThread using function object as callable: "<<i<<"\n";
	}
	void name(){
		cout <<"\nPrinting name. " << endl;
	}

	void address(int y)
	{
		cout <<"\nPrinting Address: "<< y << endl;
	}
};

int main()
{
	cout << "Threads 1 and 2 and 3 operating independently \n" << endl;
	thread th1(foo, 2);	    // The thread (th1) is launched by using function pointer (foo) as callable
	thread th2(thread_obj(), 3);	// The thread (th2) is launched by using function object (thread_obj) as callable
	thread_obj t1;
	t1.name();

	// Lambda Expression
	auto f = [](int x) {for (int i = 0; i < x; i++) cout << "\nThread using lambda expression as callable: "<<i<<" \n"; };

	thread th3(f, 5);	// This thread is launched by using lamda expression as callable
	// Wait for the threads to finish 
	th1.join();	// Wait for thread t1 to finish
	th2.join();	// Wait for thread t2 to finish
	th3.join();	// Wait for thread t3 to finish

	system("pause>0");
	return 0;
}

// pthread_create (thread, attr, start_routine, arg)
// 1. thread: An opaque, unique identifier for the new thread returned by the subroutine.
// 2. attr: An opaque attribute object that may be used to set thread attributes.
// 	You can specify a thread attributes object, or NULL for the default values.
// 3. start_routine: The C++ routine that the thread will execute once it is created.
// 4. arg: A single argument that may be passed to start_routine.
// 	It must be passed by reference as a pointer cast of type void. NULL may be used if no argument is to be passed.