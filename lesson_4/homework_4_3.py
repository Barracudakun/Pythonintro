# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable
#
# string_1 = "i am going to have a good breakfast at Quincy"
# char_1 = "o"
#
# #method 1
# result_1 = string_1.count(char_1)
# print(f'result_1 = {result_1}')
#
# #method 2 for loop
# result_1 = 0
# for char_1 in string_1:
#     if char_1 == 'o':
#        result_1 += 1
#
# print(f'result_1 = {result_1}')
#
# # #method 3 while loop
# result_1 = 0
# counter = 0
#
# while counter < len(string_1):
#     if string_1[counter] == char_1:
#         result_1 += 1
#     counter += 1
# print(result_1)







# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = '234'
result_2 = 1
counter = 0

while counter < len(number_1):
    result_2 *= int(number_1[counter])
    counter += 1
print(result_2)




# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

#method 1
# number_2 = input('num:')
# result_3 = number_2[::-1]
# print(result_3)

#method 2
'''
# Ask for enter the number from the use
number = int(input("Enter the integer number: "))

# Initiate value to null
revs_number = 0

# reverse the integer number using the while loop

while (number > 0):
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

# Display the result
print("The reverse number is : {}".format(revs_number))


'''
