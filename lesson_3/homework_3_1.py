# Enter two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

# first_number = int(input('first:'))
# second_number = int(input('second:'))
#
# if first_number > second_number:
#     result_1 = first_number
#
# else:
#     result_1 = second_number
#
# print(f'result_1 = {result_1}')

'''
# definition
# first_number = int(input('first:'))
# second_number = int(input('second:'))

# def greaternumber(first_number,second_number):
#     first_number = int(input('first:'))
#     second_number = int(input('second:'))
#     if first_number > second_number:
#         result_1 = first_number
#         return result_1
#     else:
#         result_1 = second_number
#         return result_1
#
# print(first_number)
'''


# Enter a random number in number_1 variable. If this number is 20 or
# higher save “Too high” text to result_2, otherwise save “Thank you”.

# number_1 = int(input('num:'))
#
# if number_1 >= 20:
#     result_2 = 'too high'
# else:
#     result_2 = 'Thank you'
#
# print(f'result_2= {result_2}')


# Enter your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

# first_name = 'Yingxu'
# last_name = 'Yao'
#
#
# if len(first_name) < 5:
#     result_3 = str.upper(f'{first_name}{last_name}')
#
# else:
#     result_3 = str.lower(first_name)
#
# print(result_3)




# Enter a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = int(input('num:'))
result_4 = None

if 10 <= number_2 <= 20:
    result_4 = "Thank you"
    print(number_2, result_4)

else:
    result_4 = "Incorrect answer"
    print(result_4)

# Enter your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = None
result_5 = None


# Enter a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_month in lower case

month = None
result_month = None