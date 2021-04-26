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

# Additional Exercises:

print('\n ## Task 6 ## \n')
# Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.


def show_numbers(limit):
    for i in range(limit):
        msg = "EVEN" if i % 2 == 0 else "ODD"
        print(i, msg)


show_numbers(11)

print('\n ## Task 8 ## \n')
# Create a class named Person, with firstname and lastname properties, and a print name method.


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        name = self.first_name + " " + self.last_name
        print(f"Name is {name}")


john = Person('John', 'Travolta')
john.print_name()

somebody = Person('Michael', 'Hessle')
somebody.print_name()

print('\n ## Task 9 ## \n')
# Write a program asks for numeric user input. Instead the user types characters in the input box. The program normally would crash. But write try-except block so it can be handled properly.

while True:
    try:
        user_input = int(input("Please enter an integer value: "))
        break
    except ValueError:
        print("Not a valid integer! Please tra again")
print("You have entered an integer value, Good Job!")

print('\n ## Task 10 ## \n')
# Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said class


class Student:
    pass


class Marks:
    pass


martin = Student()
print(martin)

stud1_marks = Marks()
print(stud1_marks)

print(f"martin instance of class Student: {isinstance(martin, Student)}")
print(f"martin instance of class Marks: {isinstance(martin, Marks)}")
print(
    f"stud1_marks instance of class Student: {isinstance(stud1_marks, Student)}")
print(
    f"stud1_marks instance of class Marks: {isinstance(stud1_marks, Marks)}")

print(
    f"Student subclass of built in object class: {issubclass(Student, object)}")
print(
    f"Marks subclass of built in object class: {issubclass(Marks, object)}")
