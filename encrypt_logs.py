import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

AlphaToNum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
              'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
              'y': 24, 'z': 25, ' ': 26, '.': 27, ',': 28, 'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34,
              'G': 35, 'H': 36, 'I': 37, 'J': 38, 'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43, 'P': 44, 'Q': 45,
              'R': 46, 'S': 47, 'T': 48, 'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54, '1': 55, '2': 56,
              '3': 57, '4': 58, '5': 59, '6': 60, '7': 61, '8': 62, '9': 63, '0': 64, '-': 65, '/': 66}
# AlphaToNum is a library for one to one translation of letters to numbers

RandomizeNumToLetter = {"a": 13, "b": 49, "c": 2, "d": 62, "e": 47, "f": 10, "g": 15, "h": 55, "i": 24, "j": 56,
                        "k": 59, "l": 34, "m": 61, "n": 54, "o": 60, "p": 4, "q": 42, "r": 30, "s": 58, "t": 21,
                        "u": 5, "v": 57, "w": 23, "x": 48, "y": 65, "z": 20, ".": 26, " ": 27, ',': 12, 'A': 64,
                        'B': 51, 'C': 35, 'D': 31, 'E': 43, 'F': 50, 'G': 44, 'H': 38, 'I': 8, 'J': 9, 'K': 53, 'L': 16,
                        'M': 29, 'N': 45, 'O': 32, 'P': 3, 'Q': 11, 'R': 41, 'S': 39, 'T': 46, 'U': 0, 'V': 33, 'W': 63,
                        'X': 14, 'Y': 28, 'Z': 40, '1': 7, '2': 22, '3': 37, '4': 19, '5': 18, '6': 1, '7': 17, '8': 6,
                        '9': 52, '0': 36, '-': 25, '/': 66}
# RandomizeNumToLetter is a randomized number to letter library

sng_import = open('Song_Temptation_Of_Adam.txt', 'r')
Song = sng_import.read()
sng_import.close()

n = 0

p = []


def encrypt1(plaintext):
    """
    encrypt1 uses an integer variable to add one number to the numerical value of each letter in the string,
    incrementing each letter integer value by one. It then uses the InverseRandomizeNumToLetter library to randomly
    assign the incremented numbers to a letter. Then each letter is added to an array,
    which then is made into a string. the string is then reversed and added to isaiah_log
    I will explain every step in this specific step, then add sparse comments to the other methods
    becuase other than FUTURE: 3, the methods are similar
    """
    for pt_letter in plaintext:
        pt_number = AlphaToNum[pt_letter] # converts letter to corresponding number
        global n # calls on a variable for incrementing that I use throughout the program, so it is global
        ct_number = (pt_number + n) % 66 # adds the lettertonumber to n, then mods it by 66
        n += 1  # increments n
        ct_letter = InverseRandomizeNumToLetter[ct_number] # runs the combined number through te random library
        p.append(ct_letter) # adds this letter to an array for storing each letter until it is passed to the log
    ct_string = ''.join(p)  # joins the array together into a string
    inv_ct_string = rev_str(ct_string)  # reverses the string
    p.clear()  # clears the array p for later use
    i = open('isaiah_log.txt', '+a') # opens the log I am aiming to add too
    i.write(inv_ct_string) # writes this string to the log
    i.write('\n')  # adds a return to isaiah_log so another addition will be added to a new line
    i.close() # shuts the log becuase it is done writing
    n = 0  # resets the incrementing integer to zero


def encrypt2(plaintext):
    """
    encrypt2 uses the lyrics of 'The Temptation of Adam' by Josh Ritter to encrypt gift_ideas. It adds the AlphaToNum
    values of the incrementing lyric letter to the AlphaToNum value of the message letter then mods it by 66, runs it
    back through the theoretically random InverseRandomizeNumToLetter and reversing the string before adding
    it to gift_ideas.
    """
    for pt_letter in plaintext:
        pt_number = AlphaToNum[pt_letter]  # takes the letter and changes it to a corresponding number
        global n
        song_letter = Song[n]  # calls on incrementing indexes of the song lyrics
        song_num = AlphaToNum[song_letter]
        ct_number = (pt_number + song_num) % 66
        n += 1
        ct_letter = InverseRandomizeNumToLetter[ct_number]
        p.append(ct_letter)
    ct_string = ''.join(p)
    inv_ct_string = rev_str(ct_string)
    p.clear()
    i = open('gift_ideas.txt', '+a')
    i.write(inv_ct_string)
    i.write('\n')
    i.close()


def encrypt3(plaintext):
    """
    encrypt3 uses Fernet symmetric encryption to encrypt my college essay ideas for people. This obviously has to be
    the most secure because it is the first thing people would check if I were to get hacked. It uses a password
    that can be set in the code here. In this case, it is 'colleges'. Then, the string of
    encrypted text is trimmed for easier decryption and then is passed to essay_ideas.
    """
    password_provided = input('password:')  # provides input for what password must be entered to access plaintext
    if password_provided != 'colleges':
        print('you have entered the incorrect password. Goodbye')
        quit
    fernet_password = password_provided.encode()
    salt = b'colleges'  # provides what the password should be
    # This creates a hash key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # safely stores the password using the hash key and the user input
    key = base64.urlsafe_b64encode(kdf.derive(fernet_password))
    message = plaintext.encode()
    cipher_suite = Fernet(key)  # stores the specific key for encryption
    cipher_text = cipher_suite.encrypt(message)
    ct_string = str(cipher_text)  # turns the byte CipherText3 type to a string
    # the next three lines remove the b'' indicating that the string is a byte form for later decryption
    ct_string = ct_string[1::]
    ct_string = ct_string[1::]
    ct_string = ct_string[:-1:]
    i = open("essay_ideas.txt", "a+")
    i.write(ct_string)  # writes the message to essay_ideas
    i.write('\n')
    i.close()


letters = []


def decrypt1():
    """
    decrypt1 decrypts the encryption from encrypt1 in a backwards fashion.
    """
    org_msg = open('isaiah_log.txt', 'r')
    ct_lines = org_msg.readlines()
    for inv_ct_string in ct_lines:
        ct_string = rev_str(inv_ct_string)
        for Ct_Letter in ct_string:
            if Ct_Letter == '\n':
                global letters
                letters.append('\n')
            else:
                ct_number = RandomizeNumToLetter[Ct_Letter]
                global n
                pt_number = (ct_number - n) % 66
                n += 1  # increments n
                pt_letter = InverseAlphaToNum[pt_number]
                letters.append(pt_letter)
                message_final = ''.join(letters)
        n = 0
    print(message_final)
    org_msg.close()
    letters = []


message = []


def decrypt2():
    """
    decrypt2 accomplishes a similar task to decrypt1 in that it reverses the encryption from encrypt1
    completely backwards.
    """
    org_msg = open('gift_ideas.txt', 'r')
    ct_lines = org_msg.readlines()
    for Inv_Ct_String in ct_lines:
        ct_string = rev_str(Inv_Ct_String)  # reverses the string of CipherText
        for ct_letter in ct_string:
            if ct_letter == '\n':
                global message
                message.append('\n')
            else:
                global n
                song_letter = Song[n]  # gains the incremented letters for each pass in the song text
                n += 1
                # uses the same process as in decrypt1 to reverse the letter to number encryption
                ct_number = RandomizeNumToLetter[ct_letter]
                pt_number = (ct_number - AlphaToNum[song_letter]) % 66
                pt_letter = InverseAlphaToNum[pt_number]
                message.append(pt_letter)
                message_final = ''.join(message)
        n = 0
    print(message_final)
    org_msg.close()
    message = []


m = []


def decrypt3():
    password_provided = input('password:')
    fernet_password = password_provided.encode()
    # next lines are for creating the hash key using the password 'colleges'
    salt = b'colleges'
    if password_provided != 'colleges':
        print('you have entered the incorrect password. Goodbye')
        quit
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(fernet_password))
    cipher_suite = Fernet(key)  # uses Fernet to create a key in this specific line
    org_msg = open('essay_ideas.txt', 'r')
    # reads off the lines for essay_ideas so each message will be decrypted starting from the beginning
    ct_lines = org_msg.readlines()
    for Ct_String in ct_lines:
        coded_ct_string = Ct_String.encode()
        byte_pt_string = cipher_suite.decrypt(coded_ct_string)  # decrypts the message using the Fernet decrypt method
        pt_string = str(byte_pt_string)  # like in encrypt3, this changes the byte type message into a string
        # next three lines once again trim down the message so it is more easily digestible by the reader
        pt_string = pt_string[1::]
        pt_string = pt_string[1::]
        pt_string = pt_string[:-1:]
        global m
        m.append(pt_string)
        m.append('\n')
    pt_return = ''.join(m)  # joins the decrypted lines to the final message to be returned
    pt_return = pt_return[:-1:]
    print(pt_return)
    org_msg.close()
    m = []


# rev_str is a simple reverse string function
def rev_str(s):
    return s[::-1]


InverseRandomizeNumToLetter = {v: k for k, v in RandomizeNumToLetter.items()}
InverseAlphaToNum = {v: k for k, v in AlphaToNum.items()}

Count_Wrong_Auth = 0
'''
This next part is the skeleton of the actual code running. It checks for a password then asks what log the user 
wants to access. Then it asks if they would like to read or write. If they want to write they can, and it will be 
passed, encrypted, to the specified file. If they want to read, the system will decrypt the message they want and 
will return it to them. If there is a bad command or password, it will not accept it.
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
            if Count_Wrong_Auth >= 2:
                break
            Count_Wrong_Auth = Count_Wrong_Auth + 1
            print('you have ' + str(3 - Count_Wrong_Auth) + ' more attempts')
else:
    print('wrong password, goodbye')
