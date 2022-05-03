#include <iostream>

using namespace std;

int main()
{

    // game loop
    while (1) {
        string enemy1; // name of enemy 1
        cin >> enemy1; cin.ignore();
        int dist1; // distance to enemy 1
        cin >> dist1; cin.ignore();
        string enemy2; // name of enemy 2
        cin >> enemy2; cin.ignore();
        int dist2; // distance to enemy 2
        cin >> dist2; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"

        // Enter the code here
        if (dist1 < dist2) {
        cout << enemy1 << endl;
}  else {
    cout << enemy2 << endl;
}

    }
}

// main:	if pinC.0 = 1 then
// 	  goto flsh		; jump to flsh if pin0 is high
// 	else
// 	  goto main		; else loop back to start
// 	endif

// flsh:	high B.1		; switch on output B.1
// 	pause 5000		; wait 5 seconds
// 	low B.1			; switch off output B.1
// 	goto main		; loop back to start