# Importing the necessary functions from the modules.
from random import choice

printable = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",'r',"s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","#","$","%","&","*","+","-",".","/",":",";","<","=",">","?","@","^","_",",","|", " "]

try:

    length = int(input("Enter the desired length of the password: "))
    
    # Selects a random valid character and adds it to the password.
    password = "".join(choice(printable) for _ in range(length))

    print(f"The password is {password}")

except ValueError:

    print("Please enter a valid value.")