'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in old_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

# [ expression for item in list if conditional ]

# This is equivalent to:

'''for item in list:
    if conditional:
        expression '''
		
		


#Which corresponds to:

#*result*  = [*transform*    *iteration*         *filter*     ]

#The filter part answers the question if the item should be transformed. '''

#class way
old_list = [1,2,3,4,5]
new_list = []

for i in old_list:
    i = i**2
    new_list.append(i)

print(new_list)

new_list = [i**2 for i in old_list]

#for i is iterator
#old list is filter
#i**2 is transform expression
print(new_list)

#1) creating a simple list of 10 numbers using Range()
x = [i for i in range(10)]
print(x)
# Output -[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]





#2) creating a list that evaluates an expression
squares = [x**2 for x in range(10)]
print(squares)
# Output -[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



#3) creating a list from another list
list1 = [3,4,5]

multiplied = [item*3 for item in list1]
print(multiplied)
#[9,12,15]

# 4) using list comprehension for string manipulation
listofwords=['this', 'is', 'a', 'list', 'of', 'words']
items = [word[0] for word in listofwords] #index gives first letter of each word
print(items)
# Output - ['t', 'i', 'a', 'l', 'o', 'w']



# 5) Let's show how easy you can convert lower case / upper case letters.
output = [x.lower() for x in ['A', 'B', 'C']]
print(output)

#Output 1 - ['a', 'b', 'c']

output2 = [x.upper() for x in ['a','b','c']]
print(output2)
# Output 2 - ['A', 'B', 'C']





#6) Creating a list based on a condition



#Output - [0, 4, 16]




# 7) Extracting numbers only from a string and putting it in a list



# Output - ['1', '2', '3', '4', '5']




#8
''' 
In this example, we can see how to get specific lines out from a text file. 

Create a text file and put in some text in it. 

this is line1
this is line2
this is line3
this is line4
this is line5

Save the file as test.txt '''





#Output: ['this is line3']



#9) Using functions in list comprehension

# Create a function and name it double:


# If you now just print that function with a value in it, it should look like this:



# Answer - 20


#We can easily use list comprehension on that function.





# Output - [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]






# 10) adding an IF condition to the above





# Output - [0, 4, 8, 12, 16]






# 11) You can add more arguments (using multiple iterators and lists):





# Output - [30, 50, 70, 50, 70, 90, 70, 90, 110]



















		
		

