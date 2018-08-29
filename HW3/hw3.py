# Name:
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 

# Define your function here
##### YOUR CODE HERE #####
def list_intersection(list1, list2):
    list_int = []
    for i in list1:
        if i in list2:
            list_int.append(i)
    return list_int

print list_intersection([3,5], [4,5,6])

print list_intersection([2,3], [3,3,3,2,10])

print list_intersection([4,5], [3,3,3,2,10])

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####

# **********  Exercise 3.2 **********

# Define your function here
def ball_collide(ball1, ball2):
    ##### YOUR CODE HERE #####
    return "Not Yet Implemented"

# Test Cases for Exercise 3.2
# print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
# print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
# print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {}

def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    #return "Not Yet Implemented"
    my_classes[class_num] = desc

# Here, use add_class to add the classes you're taking next term
#add_class('6.189', 'Introduction to Python')
add_class('2.40', 'CS1')
add_class('2.41', 'CS2')
add_class('4.40', 'Programming Languages')

def print_classes(course):
    ##### YOUR CODE HERE #####
    #return "Not Yet Implemented"
    for i in my_classes.keys():
        if i.startswith(course + "."):
            print i,"-",my_classes[i]


# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####
print_classes('4')

# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(a1, a2):
    comb_dict = {}
    ##### YOUR CODE HERE #####
    for i,j in zip(a1, a2):
        if (i not in comb_dict):
            comb_dict[i] = []
        comb_dict[i].append(j)
    return comb_dict

# combined_dict = combine_lists(??, ??) # Finish this line...
combined_dict = combine_lists(AGES, NAMES)
print combined_dict

def people(age):
    # Use combined_dict within this function...
    return "Not Yet Implemented"

# Test Cases for Exercise 3.4 (all should be True)
#print 'Dan' in people(18) and 'Cathy' in people(18)
#print 'Ed' in people(19) and 'Helen' in people(19) and\
#       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
#print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
#print people(21) ==   ['Bob']
#print people(22) ==   ['Kelly']
#print people(23) ==   []

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    ##### YOUR CODE HERE #####

    return "Not Yet Implemented"

# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == "Sunday" # This should be True
##### YOUR CODE HERE #####
