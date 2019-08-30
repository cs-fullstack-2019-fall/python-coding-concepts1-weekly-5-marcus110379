### Problem 1:
# #Ask a user for the year they were born by calculating their age. Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”
# # yearBorn = int(input("what year were you born?"))
# # age = 2019 -yearBorn
# # print(f"you are {age}  years old")


### Problem 2:
#Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”

# userInput = input("Enter a name")
# if userInput == "Kenn":
#     print("Hello Teacher")
# elif userInput == "Kevin":
#     print("Hello Teacher")
# elif userInput == "Erin":
#     print("Hello Teacher")
# elif userInput == "Autumn":
#     print("Hello Teacher")
# else:
#     print("Hello Student")


## Problem 3:
# Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.

# userInput = int(input("enter a negative number"))
# for i in range(7, userInput -1, -1):
#     print(i)

### Problem 4:
# Ask the user to enter a number between -10 to -5. If their input is not between the two numbers ask them to do
# it again until they get it right. Afterward they print the correct number, print "Good job"

userInput = int(input("enter a number between - 10 to -5"))
while userInput > -5 and  userInput > -10:
    userInput = int(input("enter a number between - 10 to -5"))
print("Good job")


### Problem 5:
#Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.
# squad = ["One", "Two", "Three", "Four", "Five"]
# for i in range(len(squad)-1, -1, -1 ):
#     print(squad[i])

## Problem 6:
# Create a function that will have the string firstName as a parameter. In the function ask the user for their last name.
# Print "Hello [FIRST & LAST NAME]" in the function. Call that function

# def problem6(fName):
#     userInput = input("what is your last name ")
#     print(f"Hello {fName} {userInput}")
# problem6("marcus")

### Problem 7:
# Create the class Books with name, rating, genre, and author properties/attributes.
# Create a class method that will change the rating of the book. Outside of the class, create three objects of the class Book and put them in an array.
# Lastly, USING THE ARRAY print only the names of the books using any method we’ve learned in class.
#

# class Books:
#     def __init__(self,name, rating, genre,  author ):
#         self.name = name
#         self.rating = rating
#         self.genre =genre
#         self.author = author
#     def changeRating(self,rating):
#         self.rating = rating
#
#     def __str__(self):
#         return f""
#
# mybook1 = Books("pop","5", "fiction","bach")
# mybook2 = Books("roadies","5", "fiction","mitchell")
# mybook3 = Books("life","4", "fiction","smith")
#
# bookNames = [mybook1, mybook2, mybook3]
# for i in bookNames:
#     print(i)


### Problem 8:
# Create a function that asks the user to enter a number. If the number is between and include -50 and 5, return "Funds too low".
# If the number is between 5 and 50, return “You should add more funds.” If the number is more than 50, return “Just enough.”

# def ask():
#     userInput = int(input("enter a number"))
#     if userInput >= -50 and userInput <= 5:
#         return "Funds are too low"
#     elif userInput >= 5 and userInput <= 50:
#         return "You should add more funds."
#     elif userInput > 50:
#         return "Just enough"
# ask()

## Problem 9:
# Ask the user for a positive number. Create an empty array and starting from zero, add each number by 1 into the array.
# Print EACH ELEMENT of the array.
# userInput = int(input("enter a positive number"))
# number = []
# for i in range(0, userInput + 1,1 ):
#     number.append(i)
#
# print(number)

### Problem 10:
# Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property.
# Include a method that will print each attribute/property. Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.



# class Pet:
#     def __init__(self, type, breed):
#         self.type = type
#         self.breed = breed
#
#     def printAll(self):
#         print(f"{self.type},{self.breed}" )
#
#
# myDog1 =Pet("dog", "doberman")
# myDog2 =Pet("dog", "shepherd")
# myDog3 =Pet("dog", "greyhound")
# pet_list = [myDog1,myDog2,myDog3]
# myDog1.printAll()
# myDog2.printAll()
# myDog3.printAll()