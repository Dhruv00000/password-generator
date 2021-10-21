# Importing the necessary functions from the modules.
from random import choice

chars = []

try:

    # Getting the user input.
    length = int(input("Enter the desired length of the password: "))
    special = input("Enter yes if you want special characters in the password and enter no if not: ").lower()
    whitespaces = input("Enter yes if you want spaces in your password and no if not: ").lower()
    numbers = input("Enter yes if you want numbers in your password and no if not: ").lower()
    characters = input("Enter yes if you want characters in your password and no if not: ").lower()
    custom = input("Enter any custom characters separated by a comma (leave blank if you dont want custom characters): ")

    # Generating the list of characters for the password.
    if "," in custom:

        customWords = custom.split(",")
        chars += customWords

    if special != "no":

        chars += ["!","#","$","%","&","*","+","-",".","/",":",";","<","=",">","?","@","^","_",",","|"]

    if numbers != "no":

        chars += ["0","1","2","3","4","5","6","7","8","9"]

    if whitespaces == "yes":

        chars += [" "]

    if characters != "no":

        chars += ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",'r',"s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    # If the user selects nothing to add to the password, this message is printed out.
    if not chars:

        print("You must select something to add in your password.")

    # Output.
    print(f"The password is {''.join(choice(choice(chars)) for _ in range(length))}")

# If the user enters a string instead of an integer, this message is printed out instead of the program crashing with an error.
except ValueError:

    print("Please enter a valid value.")