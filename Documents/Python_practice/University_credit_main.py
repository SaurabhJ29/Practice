# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:53:46 2022

@author: saura
"""

k = 3
n = 4

Stdnt_Cr_limit = [40, 50, 30, 80]
Subs_cr = [20, 30, 25]
Sub_cr = sorted(Subs_cr)
print("\nSubjects credits are: ", Sub_cr)

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

x = list(powerset(Sub_cr))
x.remove(())
print("\nAll the combinations of the subjects credits are: \n", x, "\nand the number of elements in it:", len(x))

# =============================================================================
# for x1 in x:
#     print("\nSum of the elements are: ", sum(x1), "\nnumber of elements in it:", len(x1) )
# =============================================================================

total_count = 0

for index, credit_limit in enumerate(Stdnt_Cr_limit):
    count = 0
    print("\n\nThe details of student {} is as follows:".format(index +1))
    
    for index2, j in enumerate(x):
        Cr_sub = 0
        
        if sum(j) <= credit_limit:
            
#            print("\nSubject {} credit is: ".format(index2 + 1) , sum(j))
            count += 1
   #         print("Count: ", count)

    
    print("Student {}, his credit limit is: ".format(index + 1), credit_limit)
        
    total_count += count
    
    print("Total options for the student {} are: ".format(index + 1), count)
        
print("\n\nNumber of ordered pairs are: ", total_count)