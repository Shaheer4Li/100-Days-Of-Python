alpahabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
status = "yes"
def ceaser(Text, Shift,EorD):

    def encrypt(plain_Text, Shift):
        coded = ""
        for i in plain_Text:
            if i not in alpahabet:
                coded += i
                continue
            else:
                position_in_text = alpahabet.index(i)
                new_pos = (position_in_text + Shift) % 26
                chiper = alpahabet[new_pos]
                coded+= chiper
        print(coded)
    def decrypt(cipher_text, Shifts):
        decode = ""
        for i in cipher_text:
            if i not in alpahabet:
                decode += i
                continue
            else:
                location = alpahabet.index(i)
                new_pos = (location - Shifts) % 26
                dechiper = alpahabet[new_pos]
                decode += dechiper
        print(decode)
    if EorD == "encrypt":
        encrypt(Text, Shift)
    elif EorD == "decrypt":
        decrypt(Text, Shift)
    else:
        print("Invalid input. Please type 'encrypt' or 'decrypt'.")
while status == "yes":
    print(r'''  ___ __ ____  __  __  ____ ____                            
 //   || || \\ ||  || ||    || \\                           
((    || ||_// ||==|| ||==  ||_//                           
 \\__ || ||    ||  || ||___ || \\                           
                                                            
 ____ __  __   ___ ____  _  _ ____  ______ __   ___   __  __
||    ||\ ||  //   || \\ \\// || \\ | || | ||  // \\  ||\ ||
||==  ||\\|| ((    ||_//  )/  ||_//   ||   || ((   )) ||\\||
||___ || \||  \\__ || \\ //   ||      ||   ||  \\_//  || \||''')
    eord = (input("Type encrypt to encrypt, type decrypt to decrypt: ")).lower()
    text = input("Type your message: ").lower()
    shifts = int(input("Type the shift number: "))
    ceaser(Text= text, Shift= shifts,EorD=eord)
    status = input("Do you want to do again? yes or no ").lower()