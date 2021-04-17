import random

print(' ## Task 1 ## \n')
#Write a python script to print your name and age

name = "Majid Khan"
age = int(2021-1983)
print('My name is ' + name + "\nI am " + str(age) + " years old \n")


print(' ## Task 2 ## \n')
# Create a list of your 5 favorite movies and store it in the variable
favMovies = ['The Shawshank Redemption', 'The Dark Knight ', 'Catch Me If You Can', 'The Godfather', 'For a Few Dollars More' ]
for i in range(len(favMovies)):
    print('My all time favourite movies are; \n', favMovies[i])

print('\n ## Task 3 ## \n')
# Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
print('The first color in the list is ' + color_list[0], '\nThe last color in the list is ' + color_list[-1])

print('\n ## Task 4 ## \n')
# Write a Python script to add a key to a dictionary
myDictionary = {0: 10, 1: 20}
print('Original dictionary:     ', myDictionary)

myDictionary[2] = 30
print('After adding a key:      ', myDictionary)

print('\n ## Task 5 ## \n')

weight = input('Please enter your weight:           ')
height = input('Please enter your height in meter:  ')
bmi = round(float(weight) / float(height) ** 2, 3)
# print('height in m2 ', float(height)**2)

# https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm
# A BMI of less than 18.5 means that a person is underweight.
if (bmi < 18.5):
    print('BMI:', bmi, '(Underweight)')

# A BMI of between 18.5 and 24.9 is ideal.
elif (bmi > 18.5 and bmi < 24.9):
    print('BMI:', bmi, '(Normal)')

# A BMI of between 25 and 29.9 is overweight.
elif (bmi > 24.9 and bmi < 30):
    print('BMI:', bmi, '(Overweight)')

# A BMI over 30 indicates obesity
else:
    print('BMI:', bmi, '(Obese)')
print('\n ######################### ')
print(' ## Additional Exercise ## ')
print(' ######################### \n')

print('\n ## Task 6 ## \n')
# Guess a number game - between 1 to 9.

import random
randomNo = random.randint(1, 10)
timesTry = 0
while timesTry < 10:
    guess = int(input('Please enter a number from 1 to 10:  '))
    timesTry += 1
    if randomNo != guess:
        print('Please try another number:   ')

    if randomNo == guess:
        print('Well guessed')
        break


print('\n ## Task 7 ## \n')
#Create a tuple with different data types

myTuple= (1.1, 'A', '/', 10, 'y', '+', ['mango', 'apple', 'orange'], {"name" : "Majid", "class" : "JSript"})

# print(str(i) + ' is of type' + str(type(i)))
for i in myTuple:
    print(str(i) + '        is of type  ' + str(type(i)))

print('\n ## Task 8 ## \n')
# Create a list of 5 city names and convert it into tuples.
citiesList = ['Copenhagen', 'Aarhus', 'Odense', 'Aalborg', 'Roskilde']
print('List:                        ', citiesList)
citiesTuple = tuple(citiesList)
print('List converted into tuple:   ', citiesTuple)

print('\n ## Task 9 ## \n')
# Remove duplicated from the list and store the values in the same list:
a = [10,20,30,20,10,50,60,40,80,50,40]
print('Original list:               ', a)
a = list(dict.fromkeys(a))

print('After removing duplicates:   ', a)

print('\n ## Task 10 ## \n')

# Accept a string from user and remove the characters which have odd index values of a given string and print them.

userStringInput = input('Pleas enter string: ')
result = ""
for i in range(len(userStringInput)):
    if (i % 2 == 0):
      result = result + userStringInput[i]
print("Original String:     ", userStringInput)
print("Altered String:      ", result)

