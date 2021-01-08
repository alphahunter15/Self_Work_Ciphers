import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

AlphaNum = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25, ' ' : 26, '.' : 27, ',' : 28, 'A' : 29, 'B' : 30, 'C' : 31, 'D' : 32, 'E' : 33, 'F' : 34, 'G' : 35, 'H' : 36, 'I' : 37, 'J' : 38, 'K' : 39, 'L' : 40, 'M' : 41, 'N' : 42, 'O' : 43, 'P' : 44, 'Q' : 45, 'R' : 46, 'S' : 47, 'T' : 48, 'U' : 49, 'V' : 50, 'W' : 51, 'X' : 52, 'Y' : 53, 'Z' : 54, '1' : 55, '2' : 56, '3' : 57, '4' : 58, '5' : 59, '6' : 60, '7' : 61, '8' : 62, '9' : 63, '0' : 64, '-' : 65, '/' : 66}
# AlphaNum is a library for one to one translation of letters to numbers

numToLetter = {"a": 13, "b": 49, "c": 2, "d": 62, "e": 47, "f": 10, "g": 15, "h": 55, "i": 24, "j": 56, "k": 59, "l": 34, "m": 61, "n": 54, "o": 60, "p": 4, "q": 42, "r": 30, "s": 58, "t": 21, "u": 5, "v": 57, "w": 23, "x": 48, "y": 65, "z": 20, ".": 26, " ": 27, ',' : 12, 'A' : 64, 'B' : 51, 'C' : 35, 'D' : 31, 'E' : 43, 'F' : 50, 'G' : 44, 'H' : 38, 'I' : 8, 'J' : 9, 'K' : 53, 'L' : 16, 'M' : 29, 'N' : 45, 'O' : 32, 'P' : 3, 'Q' : 11, 'R' : 41, 'S' : 39, 'T' : 46, 'U' : 0, 'V' : 33, 'W' : 63, 'X' : 14, 'Y' : 28, 'Z' : 40, '1' : 7, '2' : 22, '3' : 37, '4' : 19, '5' : 18, '6' : 1, '7' : 17, '8' : 6, '9' : 52, '0' : 36, '-' : 25, '/' : 66}
# numToLetter is a theoretically random way to translate the letters to numbers

sng_import = open('song.txt', 'r') # calls on song.txt, which is a file of the lyrics of 'the Temptation of Adam' by Josh Ritter
Song = sng_import.read() # Song is now a string with all the lyrics stored in it
sng_import.close()

n = 0

p = []
'''
encrypt1 uses an integer variable to add one number to the numerical value of each letter in the string, incrementing each letter integer value by one.
It then uses te numToLetter library to randomly assign the incremented numbers to a letter. Then each letter is added to an array, which then is made into a string.
the string is then reversed and added to isaiah_log
'''
def encrypt1(msgs):
    for msg in msgs:
        CipherText1 = AlphaNum[msg] # takes the letter and changes it to a corresponding number
        global n # calls on global variable n
        CipherText2 = (CipherText1 + n) % 66 # adds numerical value of number to n, which increses by one for each letter in the plaintext, and mods it by 66
        n += 1 # increments n
        CipherText3 = inverseNumToLetter[CipherText2] # changes the integer AlphaNum+n to a randomized letter
        p.append(CipherText3) # appends the new encrypted letter to array p
    CipherText4 = ''.join(p) # joins the array together into a string
    CipherText5 = rev_str(CipherText4) # reverses the string
    p.clear() # clears the array p for later use
    i = open('isaiah_log.txt', '+a')
    i.write(CipherText5) # adds the Ciphertext to isaiah_log
    i.write('\n') # adds a return to isaiah_log to create room for another addition
    i.close()
    n = 0 # resets the incrementing integer to zero

'''
encrypt2 uses the lyrics of 'The Temptation of Adam' by Josh Ritter to encrypt gift_ideas. It adds the AlphaNum values of the incrementing lyric letter to the AlphaNum
value of the message letter then mods it by 66, runs it back through the theoretically random inverseNumToLetter and reversing the string before adding it to gift_ideas.
'''
def encrypt2(msgs):
    for msg in msgs:
        CipherText1 = AlphaNum[msg] # takes the letter and changes it to a corresponding number
        global n 
        letter = Song[n] # calls on incrementing indexes of the song lyrics
        numl = AlphaNum[letter] # takes the letter from the song and changes it to a corresponding number
        CipherText2 = (CipherText1 + numl) % 66 # adds together the AlphaNum values of the letter of the message added and the song lyric letter
        n += 1 # increments n
        CipherText3 = inverseNumToLetter[CipherText2] # changes the conbined number value back into a letter
        p.append(CipherText3) 
    CipherText4 = ''.join(p) 
    CipherText5 = rev_str(CipherText4)
    p.clear()
    i = open('gift_ideas.txt', '+a')
    i.write(CipherText5)
    i.write('\n')
    i.close()

'''
encrypt3 uses Fernet symmetric encryption to encrypt my colllege essay ideas for people. This obviously has to be the most secure becuase it is the first thing
people would check if I were to get hacked. It uses a password that can be set in the code here. In this case, it is 'colleges'. Then, the string of 
encrypted text is trimmed for easier decrpytion and then is passed to essay_ideas.
'''
def encrypt3(msgs):
    password_provided = input('password:')
    password = password_provided.encode()
    salt = b'colleges' # provides what the passkey should be
    # This begins the creation of a key
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt, # stores the value of the passkey
    iterations=100000,
    backend=default_backend()
    ) # ends the key creation
    key = base64.urlsafe_b64encode(kdf.derive(password)) # safely stores the password
    message = msgs.encode() # encodes the message
    cipher_suite = Fernet(key) # stores the specific key for encryption
    CipherText3 = cipher_suite.encrypt(message) # uses the key to encrpyt the coded message
    CipherText4 = str(CipherText3) # turns the byte CipherText3 type to a string
    # the next three lines remove the b'' indicating that the string is a byte form for later decrpytion
    CipherText4 = CipherText4[1::]
    CipherText4 = CipherText4[1::]
    CipherText4 = CipherText4[:-1:]
    i = open("essay_ideas.txt", "a+")
    i.write(CipherText4) # writes the message to essay_ideas
    i.write('\n')
    i.close()

l = []
'''
decrypt1 decrpyts the encryption from encrypt1 in a backwards fashion. 
'''
def decrypt1(smth):
    org_msg = open(smth, 'r')
    Cts = org_msg.readlines()
    for Ct in Cts:
      CT = rev_str(Ct) # reverses the Ciphertext string
      for x in CT:
          if x == '\n':
              global l
              l.append('\n') # ensures there are not any blank returns taht mess with the decryption
          else:
              msg = numToLetter[x] # uses the same pseudo-random method of encryption in reverse, changing the letter to a number
              global n
              CipherText4 = (msg - n) % 66 # subtracts the value of n to get the AlphaNumvalue of the letter
              n += 1 # increments n 
              CipherText5 = inverseAlphaNum[CipherText4] # changes the numbers to letters with AlphaNum
              l.append(CipherText5) # adds the letter to array l 
              message_final = ''.join(l) # combines the array l to a string for printing
      n = 0
    print(message_final)
    org_msg.close()
    l = []

HARVARDmsg = []
'''
decrypt2 accomplishes a similar task to decrypt1 in that it reverses the encrpytion from encrpyt1 completely backwards.
'''
def decrypt2(smth):
    org_msg = open('gift_ideas.txt', 'r')
    Cts = org_msg.readlines() 
    for Ct in Cts:
      CT = rev_str(Ct) # reverses the string of CipherText     
      for x in CT:
          if x == '\n':
              global HARVARDmsg
              HARVARDmsg.append('\n') # same thing as in decrypt1. Ensures for no change from a return string value
          else:
              global n
              sub_letter = Song[n] # gains the incremented letters for each pass in the song text
              n+=1
              msg = numToLetter[x] # uses the same process as in decrypt1 to reverse the letter to number encryption
              before = (msg - AlphaNum[sub_letter]) % 66
              CipherText4 = inverseAlphaNum[before]
              HARVARDmsg.append(CipherText4)
              message_final = ''.join(HARVARDmsg)
      n = 0
    print(message_final)
    org_msg.close()
    HARVARDmsg = []

m =[]

def decrypt3(smth):
    password_provided = input('password:')
    password = password_provided.encode()
    # next lines are for creating the hash key using the password 'colleges'
    salt = b'colleges'
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    cipher_suite = Fernet(key) # uses Fernet to create a key in this specific line
    org_msg = open('essay_ideas.txt', 'r')
    Cts = org_msg.readlines() # reads off the lines for essay_ideas so each message will be decrpyted starting from the beginning
    for Ct in Cts:
        CT = Ct.encode()
        message_final = cipher_suite.decrypt(CT) # decrypts the message using the Fernet decrypt method
        message_final = str(message_final) # like in encrypt3, this changes the byte type message into a string
        # next three lines once again trim down the message so it is more easily digestible by the reader
        message_final = message_final[1::]
        message_final = message_final[1::]
        message_final = message_final[:-1:]
        global m
        m.append(message_final)
        m.append('\n')
    real_final = ''.join(m) # joins the decrpyted lines to the final message to be returned
    real_final = real_final[:-1:]
    print(real_final)
    org_msg.close()
    m = []
    
# rev_str is a simle reverse string function
def rev_str(s):
    return s[::-1]

inverseNumToLetter = {v: k for k, v in numToLetter.items()} # inverses NumToLetter library
inverseAlphaNum = {v: k for k, v in AlphaNum.items()} # inverses AlphaNum library

count_wrong = 0
'''
This next art is the skeleton of the actual code running. It checks for a password then asks what log the user wants to access.
Then it asks if they would like to read or write. If they want to write they can, and it will be passed, encrypted, to the specified file.
If they want to read, the system will decrypt the message they want and will return it to them.
If there is a bad command or password, it will not accept it.
'''
print('Welcome, user')
password = input('Password:')
if password == 'college':
    print('password accepted')
    while True:
        q = input('Future:')
        if q == '1':
            print('authentication accepted')
            print('Welcome, Isaiah')
            command = input('read or write:')
            if command == 'write':
                encrypt1(input('LOG:'))
                n = 0
            elif command == 'read':
                decrypt1('isaiah_log.txt')
                n = 0
            else:
                print('unexpected command, try again')

        elif q == '2':
            print('authentication accepted')
            print('Welcome, Isaiah')
            command = input('read or write:')
            if command == 'write':
                encrypt2(input('GIFT:'))
                n = 0
            elif command == 'read':
                decrypt2('resume.txt')
                n = 0
            else:
                print('unexpected command, try again')
        elif q == '3':
            print('authentication accepted')
            print('Welcome, Isaiah')
            command = input('read or write:')
            if command == 'write':
                encrypt3(input('IDEA:'))
            elif command == 'read':
                decrypt3('essay_ideas.txt')
            else:
                print('unexpected command, try again')
        elif q == 'break' or 'quit' or 'exit':
            print('Okay, exiting')
            break 
        else:
            print('leave, you sit on a throne of lies.')
            if count_wrong > 2:
                break
            count_wrong = count_wrong + 1
            print('you have' + str(3-count_wrong) + 'more attempts')
else:
  print('wrong password, goodbye')


