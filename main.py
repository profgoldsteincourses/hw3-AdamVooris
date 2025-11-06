# Add appropriate comments...such as your name, the date...
#Adam Vooris
#November 16th 2025
#This code makes a user id with their first and last name and a random number
import random

# makeID takes two strings
# and returns a new id
def makeID(firstname,lastname):
    # Extract the first inital of their first name
 firstinitial = firstname[0].upper()
    # Extract the first five ...
 last = lastname[:5].upper()
    # Get a random number between 10 and 99
 myNumber = random.randint(10,99)

    # Put it all together (concatenate)
 ID = firstinitial + last + str(myNumber)
 return ID


# main prompts the user for their first and last name
def main():
    # Ask for their first name
    firstname = input("What is your first name? ")

    # Ask for their last name
    lastname = input("What is your last name? ")

    # Call makeID
    newID = makeID(firstname, lastname)

    # Print out the newID
    print("Your new ID is:", newID)


# Function definitions above
############################
# Test code below
main()
