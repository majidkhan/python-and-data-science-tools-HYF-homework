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

print('\n ## Task 3 ## \n')
# Create a class of Jet inventory with two arguments i.e name and country. Also add the minimum 2 items in the class and print them.

# https://google.github.io/styleguide/pyguide.html#316-naming


class JetInventory:  # CamelCase is supported as naming convention for Python classes
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def print_jet(self):
        print(f"Jet name is {self.name} and made is {self.country}")


fighterJet = JetInventory('F16', 'USA')
print(fighterJet.name, fighterJet.country)

simpleJet = JetInventory('Boeing', 'USA')
simpleJet.print_jet()

print('\n ## Task 4 ## \n')
# Create notebook, import libraries and read the dataset.

print('\n ## Task 5 ## \n')
# Write a Python script to check whether a given key already exists in a dictionary.

jet_dict = {'name': 'F-35', 'country': 'USA', 'date': 2006}


def is_key_exist(jet_dict, key):

    if key in jet_dict.keys():
        #        print("Present, ", end=" ")
        print(f"Key '{key}' is Present, value = {jet_dict[key]}")
#        print("value =", jet_dict[key])
    else:
        #        print("Not present")
        print(f"Key '{key}' not present")


key = 'name'
is_key_exist(jet_dict, key)

key = 'make'
is_key_exist(jet_dict, key)
