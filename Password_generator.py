import random as r
password_list = []
# taking length of password from user
print("===============Welcome to the password generator!=============== \n")
Lenght = int(input("Enter minimum password length: \n"))
# Now taking keyword from user to base the password on
keyword = input("Enter a keyword(ex. City, Pet, Profession, Celebrity etc) to base the password on: \n")
password_list.append(keyword[0].upper())
#now Writing conditions
for i in range(1,len(keyword),1):
    match keyword[i]:
        case "i" | "l"|"L"|"I":
            password_list.append("1")
        case "e"|"E":
            password_list.append("3")
        case "p"|"P":
            password_list.append("9")
        case "o"|"O":
            password_list.append("0")
        case "a"|"A":
            password_list.append("4")
        case "s"|"S":
            password_list.append("5")
        case "b"|"B"|"D"|"d":
            password_list.append("6")
        case "z"|"Z":
            password_list.append("2")
        case _:
            password_list.append(keyword[i])

#now its time to add symbols
symbols = "!@#$%^&*()_+[]:;.,<>?/"
password_list.append(str(r.choice(symbols)))
while len(password_list)<Lenght:
    password_list.append(str(r.choice(symbols)))
#converting list to string 
final_password = "".join(password_list)
print("Your password is: ",final_password)