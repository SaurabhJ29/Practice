#include <stdio.h>
#include <iostream>

void update(int *a,int *b) {
    int addition = (*a) + (*b); //adding a & b, after dereferencing.
    int subtraction;

    if ((*a) > (*b))
    {
        subtraction = (*a) - (*b); //subtracting a & b, after dereferencing, when *a>*b
    }
    else
    {
        subtraction = (*b) - (*a); //subtracting a & b, after dereferencing, when *b>*a
    }

    *a = addition; //*a is pointing to additon
    *b = subtraction; //*b is pointing to subtraction
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}