# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable
#
# string_1 = "i am going to have a good breakfast at Quincy"
# char_1 = "o"

#method 1
# result_1 = string_1.count(char_1)
# print(f'result_1 = {result_1}')

#method 2
# result_1 = 0
# for char_1 in string_1:
#     if char_1 == 'o':
#        result_1 += 1
#
# print(f'result_1 = {result_1}')

#method 3 can't solve it
# result_1 = 0
# i = 0
#
# while i <= len(string_1):
#     if string_1 == 'o':
#         print(string_1[i])
#
#     i += 1
# print(result_1)







# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

# number_1 = int(input('num:'))
# number_1 = 123456789

result_2 = 1
i = 1
while i <= 10:
    result_2 = result_2*i
    i += 1
print(result_2)



# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = None
result_3 = None