// Importing the necessary functions from modules.
const ps = require("prompt-sync")
prompt = ps

function randInt(min, max) {

    min = Math.ceil(min);
    max = Math.floor(max);
    
    return Math.floor(Math.random() * (max - min + 1)) + min;

}

let printable = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",'r',"s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","#","$","%","&","*","+","-",".","/",":",";","<","=",">","?","@","^","_",",","|", " "]

let length = parseInt(prompt("Enter the desired length of the password: "))
let password = ""

for (i = 0; i < length; i++) {

    password += printable[randInt(printable.length())]
    console.log(`The password is ${password}`)

}