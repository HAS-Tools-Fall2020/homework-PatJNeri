# This is a practice document. It is meant to be run cell by cell to get the most
# Out of it. Good Luck!

# %%
Python_list = [7, 4, 8, 22]
# List indicies start at 0 and go up, can call with list_name[]
Months_of_Pandemic = ["March", "April", "May", "June", "July", "August", "September"]
# To list strings, use the ""

# %%
Time_Spent_Inside = len(Months_of_Pandemic)
# the Length function len() gives the length of the list

# %%
Python_list[1] = 5
# You can reassign elements of a list as if they were individual variables
# using the indicies

Python_list.insert(1, 6)
# In this case the first number is the index location to make the insert

#%%
del Python_list[1] 
# This should remove the number 6 that we added before

# %%
Python_list.append(11)
# This specifically adds to the end of a list
# You can also do this somewhat recursively by using the line
#Python_list = [4] + Python_list

#%%
Big_Numbies = 2
Python_list *= Big_Numbies
# This is a use of the * operator that works with any arithmetic operator 
# to modify a list (In this case duplicates the list)
# Errors can occur if the type of the objects and the function disagree. 

# %%
A = 5
B = 7
is_greater = (A > B)
# This is a good example of a Boolean Variable, one that returns either 
# True or False

#%%
Suup = "Supercalifragilistic"
"califrag" in Suup
# This is an example of Membership Operators, useful for searching lists or strings

#%%
# Recall the above A > B Cell. We can use the outcome of this cell as a conditional
# statement. In Python, if then statements are easy!
if is_greater == True:
    print("A is GREATER than B")
else:
    print("B is DOMINATING on A")
# Note the colon at the end of each conditional, including the else. This is needed.
# This could also be done with just 'if A > B:'

# %%
# Looking at the above Cell, there is one case where they are equal. To account, we
# can use the elif line.
A = 12
B = 12

if A > B:
    print("A is GREATER than B")
elif A == B:
    print("ITS TOO CLOSE TO CALL!!")
else:
    print("B is DOMINATING on A")
# %%
HowLong = len(Python_list)
Total = 0
b = 0
while i < HowLong:
    b = b + Python_list[i]
print (b)
# %%
