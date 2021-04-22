import random

print(' ## Task 1 ## \n')

# Write a function called fizz_buzz that takes a number
# a. If the number is divisible by 3, it should return “Fizz”.
# b. If it is divisible by 5, it should return “Buzz”.
# c. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# d. Otherwise, it should return the same number.


def fizz_buzz():
    entered_number = float(input('Enter any number: '))
    if(entered_number % 3 == 0 and entered_number % 5 == 0):
        print('FizzBuzz')
    elif(entered_number % 5 == 0):
        print('Buzz')
    elif(entered_number % 3 == 0):
        print('Fizz')
    else:
        print(entered_number)


fizz_buzz()

print('\n ## Task 2 ## \n')
# Consider a lst= [5, 10, 20] and write a try and except block to avoid IndexError.
try:
    a_list = [5, 10, 20]
    user_input_index = int(input(f"Enter index number: "))
    print(f"Index of a_list[{user_input_index}] is {a_list[user_input_index]}")
except IndexError:
    print(f"index a_list[{user_input_index}] does not exist")
