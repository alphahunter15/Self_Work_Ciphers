import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

AlphaToNum = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25, ' ' : 26, '.' : 27, ',' : 28, 'A' : 29, 'B' : 30, 'C' : 31, 'D' : 32, 'E' : 33, 'F' : 34, 'G' : 35, 'H' : 36, 'I' : 37, 'J' : 38, 'K' : 39, 'L' : 40, 'M' : 41, 'N' : 42, 'O' : 43, 'P' : 44, 'Q' : 45, 'R' : 46, 'S' : 47, 'T' : 48, 'U' : 49, 'V' : 50, 'W' : 51, 'X' : 52, 'Y' : 53, 'Z' : 54, '1' : 55, '2' : 56, '3' : 57, '4' : 58, '5' : 59, '6' : 60, '7' : 61, '8' : 62, '9' : 63, '0' : 64, '-' : 65, '/' : 66}
# AlphaToNum is a library for one to one translation of letters to numbers

RandomizeNumToLetter = {"a": 13, "b": 49, "c": 2, "d": 62, "e": 47, "f": 10, "g": 15, "h": 55, "i": 24, "j": 56, "k": 59, "l": 34, "m": 61, "n": 54, "o": 60, "p": 4, "q": 42, "r": 30, "s": 58, "t": 21, "u": 5, "v": 57, "w": 23, "x": 48, "y": 65, "z": 20, ".": 26, " ": 27, ',' : 12, 'A' : 64, 'B' : 51, 'C' : 35, 'D' : 31, 'E' : 43, 'F' : 50, 'G' : 44, 'H' : 38, 'I' : 8, 'J' : 9, 'K' : 53, 'L' : 16, 'M' : 29, 'N' : 45, 'O' : 32, 'P' : 3, 'Q' : 11, 'R' : 41, 'S' : 39, 'T' : 46, 'U' : 0, 'V' : 33, 'W' : 63, 'X' : 14, 'Y' : 28, 'Z' : 40, '1' : 7, '2' : 22, '3' : 37, '4' : 19, '5' : 18, '6' : 1, '7' : 17, '8' : 6, '9' : 52, '0' : 36, '-' : 25, '/' : 66}
# RandomizeNumToLetter is a randomized number to letter library

sng_import = open('Song_Temptation_Of_Adam.txt', 'r') 
Song = sng_import.read() 
sng_import.close()

n = 0

p = []

def encrypt1(Plaintextt):
    '''
    encrypt1 uses an integer variable to add one number to the numerical value of each letter in the string, incrementing each letter integer value by one.
    It then uses the InverseRandomizeNumToLetter library to randomly assign the incremented numbers to a letter. Then each letter is added to an array, which then is made into a string.
    the string is then reversed and added to isaiah_log
    '''
    for Pt_Letter in Plaintext:
        Pt_Number = AlphaToNum[Pt_Letter]
        global n 
        Pt_n_Number = (CipherText1 + n) % 66 
        n += 1 # increments n
        Ct_Number = InverseRandomizeNumToLetter[Pt_n_Number] 
        p.append(Ct_Number) 
    Ct_String = ''.join(p) # joins the array together into a string
    Inv_Ct_String = rev_str(Ct_String) # reverses the string
    p.clear() # clears the array p for later use
    i = open('isaiah_log.txt', '+a')
    i.write(Inv_Ct_String) 
    i.write('\n') # adds a return to isaiah_log so another addition will be added to a new line
    i.close()
    n = 0 # resets the incrementing integer to zero

def encrypt2(Plaintext):
    '''
    encrypt2 uses the lyrics of 'The Temptation of Adam' by Josh Ritter to encrypt gift_ideas. It adds the AlphaToNum values of the incrementing lyric letter to the AlphaToNum
    value of the message letter then mods it by 66, runs it back through the theoretically random InverseRandomizeNumToLetter and reversing the string before adding it to gift_ideas.
    '''
    for Pt_Letter in Plaintext:
        Pt_Number = AlphaToNum[Pt_Letter] # takes the letter and changes it to a corresponding number
        global n 
        Song_Letter = Song[n] # calls on incrementing indexes of the song lyrics
        Song_Num = AlphaToNum[letter]
        Ct_Number = (Pt_Number + Song_Num) % 66 
        n += 1
        Ct_Letter = InverseRandomizeNumToLetter[Ct_Number] #
        p.append(Ct_Letter) 
    Ct_String = ''.join(p) 
    Inv_Ct_String = rev_str(Ct_String)
    p.clear()
    i = open('gift_ideas.txt', '+a')
    i.write(Inv_Ct_String)
    i.write('\n')
    i.close()

'''
encrypt3 uses Fernet symmetric encryption to encrypt my colllege essay ideas for people. This obviously has to be the most secure becuase it is the first thing
people would check if I were to get hacked. It uses a password that can be set in the code here. In this case, it is 'colleges'. Then, the string of 
encrypted text is trimmed for easier decrpytion and then is passed to essay_ideas.
'''
def encrypt3(Plaintext):
    password_provided = input('password:') # provides input for what password must be inputed to access the Plaintext
    if password_proided != 'colleges':
        print('you ahve inputed the incorrect password. Goodbye')
        break
    password = password_provided.encode()
    salt = b'colleges' # provides what the password should be
    # This creates a hash key
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt, 
    iterations=100000,
    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # safely stores the password using the hash key and the user input
    message = Plaintext.encode() 
    cipher_suite = Fernet(key) # stores the specific key for encryption
    CipherText = cipher_suite.encrypt(message) 
    Ct_String = str(CipherText) # turns the byte CipherText3 type to a string
    # the next three lines remove the b'' indicating that the string is a byte form for later decrpytion
    Ct_String = Ct_String[1::]
    Ct_String = Ct_String[1::]
    Ct_String = Ct_String[:-1:]
    i = open("essay_ideas.txt", "a+")
    i.write(Ct_String) # writes the message to essay_ideas
    i.write('\n')
    i.close()

l = []
def decrypt1():
    '''
    decrypt1 decrpyts the encryption from encrypt1 in a backwards fashion. 
    '''
    org_msg = open('isaiah_log.txt', 'r')
    Ct_Lines = org_msg.readlines()
    for Inv_Ct_String in Ct_Lines:
      Ct_String = rev_str(Inv_Ct_String)
      for Ct_Letter in Ct_String:
          if x == '\n':
              global l
              l.append('\n')
          else:
              Ct_Number = RandomizeNumToLetter[Ct_Letter] 
              global n
              Pt_Number = (Ct_Number - n) % 66 
              n += 1 # increments n 
              Pt_Letter = inverseAlphaToNum[Pt_Number]
              l.append(Pt_Letter) 
              message_final = ''.join(l) 
      n = 0
    print(message_final)
    org_msg.close()
    l = []

HARVARDmsg = []

def decrypt2():
    '''
    decrypt2 accomplishes a similar task to decrypt1 in that it reverses the encrpytion from encrpyt1 completely backwards.
    '''
    org_msg = open('gift_ideas.txt', 'r')
    Ct_Lines = org_msg.readlines() 
    for Inv_Ct_String in Ct_Lines:
      Ct_String = rev_str(Inv_Ct_String) # reverses the string of CipherText     
      for Ct_Letter in Ct_String:
          if x == '\n':
              global HARVARDmsg
              HARVARDmsg.append('\n')
          else:
              global n
              Song_Letter = Song[n] # gains the incremented letters for each pass in the song text
              n+=1
              Ct_Number = RandomizeNumToLetter[Ct_Letter] # uses the same process as in decrypt1 to reverse the letter to number encryption
              Pt_Number = (Ct_Number - AlphaToNum[Song_Letter]) % 66
              Pt_Letter = inverseAlphaToNum[Pt_Number]
              HARVARDmsg.append(Pt_Letter)
              message_final = ''.join(HARVARDmsg)
      n = 0
    print(message_final)
    org_msg.close()
    HARVARDmsg = []

m =[]

def decrypt3():
    password_provided = input('password:')
    password = password_provided.encode()
    # next lines are for creating the hash key using the password 'colleges'
    salt = b'colleges'
     if password_proided != 'colleges':
        print('you ahve inputed the incorrect password. Goodbye')
        break
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
    Ct_Lines = org_msg.readlines() # reads off the lines for essay_ideas so each message will be decrpyted starting from the beginning
    for Ct_String in Ct_Lines:
        Coded_Ct_String = Ct.encode()
        Byte_Pt_String = cipher_suite.decrypt(Coded_Ct_String) # decrypts the message using the Fernet decrypt method
        Pt_String = str(Byte_Pt_String) # like in encrypt3, this changes the byte type message into a string
        # next three lines once again trim down the message so it is more easily digestible by the reader
        Pt_String = Pt_String[1::]
        Pt_String = Pt_String[1::]
        Pt_String = Pt_String[:-1:]
        global m
        m.append(Pt_String)
        m.append('\n')
    Pt_Return = ''.join(m) # joins the decrpyted lines to the final message to be returned
    Pt_Return = Pt_Return[:-1:]
    print(Pt_Return)
    org_msg.close()
    m = []
    
# rev_str is a simle reverse string function
def rev_str(s):
    return s[::-1]

InverseRandomizeNumToLetter = {v: k for k, v in RandomizeNumToLetter.items()} # inverses NumToLetter library
InverseAlphaToNum = {v: k for k, v in AlphToaNum.items()} # inverses AlphaToNum library

Count_Wrong_Auth = 0
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
                decrypt1()
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
                decrypt2()
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
                decrypt3()
            else:
                print('unexpected command, try again')
        elif q == 'break':
            print('Okay, exiting')
            break 
        elif q == 'quit':
            print('Okay, exiting')
            break
        elif q == 'exit':
            print('Okay, exiting')
            break
        else:
            print('leave, you sit on a throne of lies.')
            if count_wrong >= 2:
                break
            Count_Wrong_Auth = Count_Wrong_Auth + 1
            print('you have ' + str(3-count_wrong) + ' more attempts')
else:
  print('wrong password, goodbye')




