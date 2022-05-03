

x = int(input("Enter a number to check if it is a fibonacci number: "))
a, i, b = 0, 1, 1

print("\nThe fibonacci series is till the number {} is: ".format(x))

while a<=x:
    
    print("\tThe {}th number of the fibonacci series is: ".format(i), a)

    if a==x: break

    c = a + b    #sum of last 2 terms of the series
    a, b = b, c     #equating the 3rd last term with the 2nd last term,  #equating the 2nd last term with the last term
    i+=1
    

if a!=x:
    print("\nGiven number is not fibonacci, series ended.")
else:
    print("\nIt's a {}th fibonacci number, series ended.".format(i))

    