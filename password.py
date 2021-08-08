# Importing the necessary functions from the modules.
from random import choice

printable = []

try:

    length = int(input("Enter the desired length of the password: "))

    special = input("Enter yes if you want special characters in the password and enter no if not: ").lower()
    whitespaces = input("Enter yes if you want spaces in your password and no if not: ").lower()
    numbers = input("Enter yes if you want numbers in your password and no if not: ").lower()
    characters = input("Enter yes if you want characters in your password and no if not: ").lower()
    
    custom = input("Enter any custom characters separated by a comma (leave blank if you dont want custom characters): ")
    
    if "," in custom:
        
        customWords = custom.split(",")
        printable += customWords

    if special != "no":

        printable += ["!","#","$","%","&","*","+","-",".","/",":",";","<","=",">","?","@","^","_",",","|"]

    if numbers != "no":

        printable += ["0","1","2","3","4","5","6","7","8","9"]

    if whitespaces == "yes":

        printable += [" "]

    if characters != "no":

        printable += ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",'r',"s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    if special == "no" and numbers == "no" and whitespaces == "no" and characters == "no":
        
        print("You must select something to add in your password.")

    password = " "
        
    # Selects a random valid character and adds it to the password.
    for _ in range(length):
        
        password += choice(choice(printable))

    print(f"The password is {password}")

except ValueError:

    print("Please enter a valid value.")