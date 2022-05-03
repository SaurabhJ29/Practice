x = int(input("Enter a number to check if it is a fibonacci number: "))
n = int(input("Enter the number of terms for the series: "))

a, b = 0, 1

print("\nThe fibonacci series is till the {}th term is: ".format(n))
for i in range(1, n):
    
    c = a + b    #sum of last 2 terms of the series
    print("\nThe {}th number of the fibonacci series is: ".format(i), a)
    if a==x:
        print("\nIt's a fibonacci number, series ended.")
        break
    else:
        print("Given number is not a fibonacci number, series eneded.")

    a = b     #equating the 3rd last term with the 2nd last term
    b = c     #equating the 2nd last term with the last term

# Do it with try and except block.