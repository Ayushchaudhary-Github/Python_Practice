"""
This function converts miles to kilometers (km).

Complete the function to return the result of the conversion
Call the function to convert the trip distance from miles to kilometers
Fill in the blank to print the result of the conversion
Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

"""

# Question 1 :

"""
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = ___

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + ___)

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + ___)
"""

# Answer:

# 1) Complete the function to return the result of the conversion


def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile


convert_distance(55)

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = 88.0

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str((my_trip_km)*2))


# Question-2:

"""
This function compares two numbers and returns them in increasing order.

Fill in the blanks, so the print statement displays the result of the function call in order.
Hint: if a function returns multiple values, don't forget to store these values in multiple variables
"""
"""
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
___, ___ = order_numbers(100, 99)
print(smaller, bigger)
"""
# Answer-2:

# This function compares two numbers and returns them
# in increasing order.


def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


# Question-3:

# What are the values passed into functions as input called?

# Answer-3:

# Parameters

# Question-4:

"""
Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, 
it returns the message. This way, the calling line can print the message, or do something else with it if needed.
 Fill in the blanks to complete the code to make it work.
"""
"""
def lucky_number(name):
  number = len(name) * 9
  ___ = "Hello " + name + ". Your lucky number is " + str(number)
  ___
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
"""

# Answer:


def lucky_number(name):
    number = int(len(name) * 9)
    nam = "Hello " + name + ". Your lucky number is " + str(number)    
    return nam

print(lucky_number("Kay"))
print(lucky_number("Cameron"))


# Question-5:

# What is the purpose of the def keyword?

# Answer-5:

# Used to define a new function
