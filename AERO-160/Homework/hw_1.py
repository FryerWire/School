
"""
Homework 2
Maxwell Seery
"""

# # Section 1: Interpreting Code
def section_1(pay, location):
    if (location == "space"):
        print("I'll take it!")
    elif (location == "Iowa"):
        if (pay <= 100000): # Original problem said if pay < = but it should be pay <=
            print("Not interested")
        else:
            print("I'll take it!")
    elif ((location == "Texas") and (pay >= 60000)):
        print("I'll take it!")
    elif (pay >= 70000):
        print("I'll take it!")
    else:
        print("No thanks!") # Original problem had print("No thanks!" but it should be print("No thanks!")

# pay_list = [50000, 60000, 60000, 1, 80000]
# location_list = ["Iowa", "California", "Texas", "space", "New York"]

# for i in range(len(pay_list)):
#     print(f"Problem {i + 1}")
#     section_1(pay_list[i], location_list[i])
#     print("")

# Question 6
# In most cases, the order of the actual conditional statements: if, elif, and else, does not matter. This is because the code will
# look go line by line checking the conditional parameters and if it is not satisfied, then it will simply move onto the next conditional arguments
# When it comes to the parameters within the conditional order does matter. Lets say A = 1 and B = 2. If you say A < B, this is not the same as
# B < A. So the parameters or the arguments that are put inside of the conditiopnal statements matter but the general order of the conditional statements
# do not matter as much. Basically a summary would be if you consider if, elif, and else as a macro and the parameters or arguments inside of those as micro
# micro matters a lot more in the end than macro

# Question 7
# elif (location == "Texas"):
#     if (pay >= 60000):
#         print("I'll take it!")
#     else:
#         print("Not interested")

# Section 2

# Question 1
# While loops are generally used for looping over an unknown amount of elements. This is nice because there may be cases where there are large
# datasets one is needed to loop over and when some datasets are in the thousands, hundreds of thousands, or even millions, while loops help a lot
# by taking a large dataset and shrinking it down to the things the user needs out of it. However, for and while loops can be used interchangably
# just need to change some syntax

# Question 2
# For loops are generally used for looping over a known amount of elements. This is nice because when there are known amounts of datasets, 
# one can loop over it quickly and bring something relativly large down to something a lot smaller to use. Just like the while loops, for loops
# can be interchangable between the two and only require a few syntax changes

# Section 3
# x = 3
# while x > 0:
#     x = x - 1
#     print(x)

# The final value for the x varible will be zero due to how the while loop is set up.
# When x becomes 1, has one more operation because it is still greater than zero. When it loops again, x becomes zero and since 0 is
# not larger than 0 itself, the while loop will finish

# import numpy as np
# x = np.array([1, 2, 3, 4])
# for i in range(len(x)):
#     y=x[i]*2
#     print(y)

# Since x is a numpy array with 4 elements, the for loop will run only 4 times. If the length of the array was larger, it will run for 
# however amount is inside of the array do to the range function. In order for the range function to work for an array or a list, 
# there needs to be a len function which finds the lengths of of the dataset. In this case, the length is 4 making the range function run four times
# with the values of 0 to 3. The y output is simply taking the index in which the element is placed at and squares the value
# Once the range functionr reaches 3 which is the fourth index of the array, the for loop will finish running. 

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(x)):
#     print(x[i])

# This is basically the same explanation as the problem above. With x being a python list, the len function is used to determine the length of the
# size of the list. In this case the length of the list is 9. When using the range function, it will go from 0-8 as this is 9 elements in total.
# The for loop is taking each index value and finding the corresponding element and prinint it. For example, x[5] will print 6. Once all of the
# elements have been iterated through, the for loop will finsih running

# x = 16
# while x > 2:
#     x = x/2
#     print(x)

# In the case of the while loop, x starts off at 16. Since 16 is larger than x itself, the while loop will begin to run. 
# This value is now cut in half becoming 8. Again, this is larger than 2 itself and the while loop will continue to run. 
# The value of x will be cut in half during each itteration of the while loop and when the value becomes four, it will cut
# in half one more time becoming the final value of 2. When this happens, 2 is not larger than 2 and the while loop will finish running. 

x = 1
while x <10:
    x = x+x
    print(x)

# This is basically the exact opposite of the previous problem. Instead of starting at 16, this problem ends at 16. 
# The value of x starts at one where it will then be doubled in value. This will keep on happening until it reaches 16. 
# This is due to when x is equal to 8, it is still less than 10 and the while loop will run one more time making it become 16.
# Due to the value being larger than 10 now, the while loop will come to an end and finish. 

# Section 4


# pay = ____________________
# location = ____________________

# if location == "space":
#     print("I'll take it!")
# elif location == "Iowa":
#     if pay < = 100000:
#         print("I'll take it!")
#     else: 
#         print("I'll take it!")
# elif location == "Texas" and pay >= 60000:
#     print("I'll take it!")
# elif pay >= 70000:
#     print("I'll take it!")
# else:
#     print("No thanks!"
