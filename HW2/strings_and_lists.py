# Name:
# Section:
# strings_and_lists.py

import math

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers
    total = 0
    for index, num in enumerate(number_list):
        total += num
        number_list[index] = total

    return number_list

print "cumulative_sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6])
print "cumulative_sum of [1, 2, 3, 4] is:", cumulative_sum([1, 2, 3, 4])

# Test Cases
##### YOUR CODE HERE #####

# **********  Exercise 2.8 **********

def report_card():
    ##### YOUR CODE HERE #####
    num_classes = input("How many classes did you take? ")
    i = 0
    name_list = []
    grade_list = []
    while i < num_classes:
        class_name = raw_input("Name of class: ")
        class_grade = input("Grade: ")
        name_list.append(class_name)
        grade_list.append(class_grade)
        i = i + 1
    
    gpa = float(sum(grade_list)/num_classes)
    
    print "REPORT CARD:"
    i = 0
    while i < num_classes:
        print name_list[i], " - ", grade_list[i]
        i = i + 1
    print "Overall GPA ", gpa
    
    return False

#report_card()

# Test Cases
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin

    if (word[0] in VOWELS):
        print word + "hay"
    else:
        print word[1:] + word[0] + "ay"

    ##### YOUR CODE HERE #####

#pig_latin("food")
#pig_latin("eek")

# Test Cases
##### YOUR CODE HERE #####


# **********  Exercise 2.10 **********
# Test Cases
##### YOUR CODE HERE #####
print [x**3 for x in range(1,11)]
print [x+y for x in ['h','t'] for y in ['h','t']]
def print_vowels(word):
    print [i for i in word[0:] if i in VOWELS]
print_vowels("date")
print_vowels("vowels")
print [x+y for x in [10,20,30] for y in [1,2,3]]


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
