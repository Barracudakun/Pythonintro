# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1, num_2):
    result = num_1 + num_2
    print(result)
difference(4, 5)

# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    result = num_1 / num_2
    print(result)
division(4, 2)

# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

# number = int(input('num:'))
#
# def function_1(number):
#     if number > 10:
#         result = 100 - number
#         print(result)
#     else:
#         result = number * 10
#         print(result)
# function_1(number)






# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temerature_convertor(fahrenheit_degree):
    # return (fahrenheit_degree - 32) * 5/9
    Celsius = (fahrenheit_degree - 32) * 5/9
    return Celsius

print('Celsius is',temerature_convertor(100))


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
    pass

# examples of usage:
# taxi_fare(10) #21.86