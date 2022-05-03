#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create New Jupyter Notebook command from the Command Palette (Ctrl+Shift+P) in vscode.
import time


# In[2]:


def creating_tuple(n):
    t = []
    for i in range(0, n):
        x = int(input("Enter it's value: "))
        t.append(x)
    tpl = tuple(t)
    return tpl


# In[3]:


k = int(input("Enter the no. of Subjects: "))
print("Enter the credits of the {} subjects: " .format(k))
Subs_cr = creating_tuple(k)

print(Subs_cr)
print(Subs_cr[0])
print(k)


# In[4]:


Sub_cr = sorted(Subs_cr)
print(Sub_cr)


# In[6]:


n = int(input("Enter the number of the students: "))
print("Enter the credit limit of each {} students" .format(n))
Stdnt_Cr_limit = creating_tuple(n)


# In[7]:


print("The number of subjects are: ", k, "\nCredits of these subjects are: ", Subs_cr,
      "\nNumber of students are: ", n, "Credit limits of these students are: ", Stdnt_Cr_limit)


# In[8]:


print((Subs_cr[2]))
print((Sub_cr[2]))


# In[20]:


Stdnt_sub_pair = []
for i in Sub_cr:
    for j in Stdnt_Cr_limit:
        if j>=i:
            t = (j, i)
            Stdnt_sub_pair.append(t)
            
print("The (student, subject) pairs as per the credit limits are: \n", Stdnt_sub_pair)
print("\nThe total numbers of (student, subject) pairs as per the credit limits are: ", len(Stdnt_sub_pair))


# In[21]:


Sub_stdnt_pair = []
for i in Stdnt_Cr_limit:
    for j in Sub_cr:
        if j<=i:
            p = (j, i)
            Sub_stdnt_pair.append(p)
            
print("The (subject, student) pairs as per the credit limits are: \n", Sub_stdnt_pair)
print("\nThe total numbers of (subject, student) pairs as per the credit limits are: ", len(Sub_stdnt_pair))


# In[ ]:


start_time = time.time()

count, total_count = 0, 0
total = 0

for i in range(0, n):
    p, Cr_sub = 0, 0
    print("\n\nFor the {}th student: ".format(i+1))
    
    for j in range(p, k):
        print("\n{}th subject credit is: ".format(j+1) , Sub_cr[j])
        
        if (Cr_sub + Sub_cr[j]) <= Stdnt_Cr_limit[i]:
            print("Previous count: ", count)
            count+= 1
            print("Count: ", count)
            
#         print("Subjects counts: ", count)
            
        Cr_sub+= Sub_cr[p]
        p+= 1
    
        print("Subjects credit added: ", Cr_sub)
    total_count += count
    total += 1
    print("Total count for the {}th student".format(i+1), total_count, "\t", total)
        
print("\n\nNumber of ordered pairs are: ", count, total_count)
print("Total number of subject are: ", p, " and the total credits of the subjects is: ", Cr_sub)

print("--- %s seconds ---" % (time.time() - start_time))

