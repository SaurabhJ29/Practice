#include <iostream>
using namespace std;

class SequentialAccess
{
    public:
    virtual bool HasNext() = 0;
    virtual string Next() = 0;
    virtual ~SequentialAccess() {};
};

class UsersSequentialAccess : public SequentialAccess
{
    private:
    int position;
    int size;
    string *users;

    public:
    UsersSequentialAccess(string *users, int size)
    {
        this->users = users;
        this->position = 0;
        this->size;
    }
    bool HasNext(){
        return position < size;
    }

    string Next(){
        string item = users[position];
        position++;
        return item;
    }
};

int main()
{
    string users[] = {"Tom", "Bob", "Joe", "Martin"};
    UsersSequentialAccess *sa = new UsersSequentialAccess(users, 4);

    while (sa->HasNext())
    {
        cout << sa->Next() << "\n";
    }
}