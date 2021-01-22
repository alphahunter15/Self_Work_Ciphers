# UCSB-CCS-Computing
### Simple. Secure. Expandable
* [UCSB-CCS-Computing](#ucsb-ccs-computing)
  * [Motivation](#motivation)
  * [Methods Used](#methods-used)
    * [Randomized Library](#randomized-library)
    * [Incrementing Ceasar Shift](#incrementing-ceasar-shift)
    * [Vigenere Encipherment](#vigenere-encipherment)
    * [Python Cryptographic Methods](#python-cryptographic-methods)
  * [Features And Possible Expansions](#features-and-possible-expansions)
  * [Examples](#examples)
  * [Installation](#installation)
  * [Tests](#tests)
  * [How To Use](#how-to-use)
  * [Where This Can Be Improved](#where-this-can-be-improved)
  * [Contribute](#contribute)
  * [Credits](#credits)


# Motivation
### Any great endeavor begins with the spark of human interest
Last year I attended a presentation given by Dr. Adrienne Mannov, an anthropologist who specializes in emerging cryptographic technologies. She was calling for a more trustworthy and understandable crypto-system, and explaining how we could achieve it. She asked: How can people put trust in a crypto-system if they do not understand it? I was inspired by her talk and immediately started brainstorming ideas for a more trustworthy crypto-system. Although this is an extremely rudimentary first effort at creating an understandable crypto-system, It has ade clear the difficulties of building a robust and secure yet understandable system. Especially in the case of my program, even if a "hacker" only had my methods and not my randomized library and the specific numbers I use when encrypting, a general understanding would make a brute-force attack on my system would be made very easy. So my experience with Dr. Mannov has galvanized me to create this, which has inspired me to continue my quest for the system she prophecised.
### CyberPatriot
As stated in my letter of intent, I recently founded a chapter of CyberPatriot, a cybersecurity competition team, at my high school. Our national placement of 351st out of 2376 has deepened my enthusiasm. Our early success has made clear that this work only gets more intriguing the more complex and difficult the problems become. What I have made is an early attempt in solving some problems I see in our virtual machines during competitions. For example, a common question asked of us is to find a hidden massage in a file. These usually are relatively easy to solve. Now imagine if one had found the supposed hidden message, but it was so well encrypted that the intruder didn't even know that it was what he was looking for. That is my goal and that is what I am striving towards with this program.
# Methods Used
### Randomized Library
Methods one and two utilize a randomized letter to number library to theoretically jumble the letters after they complete their unique method of initial encryption.
### Incrementing Ceasar Shift
Method one simply caesar shifts the message one further each time before passing it through the randomized library.
### Vigenere Encipherment
Method two (before using the randomized library) is in essence a Vigenere Cipher with an extremely long key. They key, in fact, is the lyrics to my favorite song, *The Temptation of Adam* by Josh Ritter.
### Python Cryptographic Methods
Installed and used from the Python3.6 repository. These are downloaded to allow the usage of Fernet Encryption for method 3 in my program.
# Features And Possible Expansions
* Three different methods of encryption.
* Simple installation and running process.
* Supported by Linux and Windows.
* Ability to expand to socket-to-socket communication becuase the message is transmitted encrypted to the file, so in the future, the program can be extended by sending the text simply to a server to store in a larger database as opposed to beign stored in a local file.
* Ability to expand to user-based interface in which multiple users exist with different passwrods and logs they can create. This would not be difficult to implement, just there would need to be an added passwd file and then some working with the main skeleton of the program to allow for a user and password input.
# Examples
This is an example of a few of the methods that can be run and what it looks like. Becuase I will have emptied out my log files for you to use, this shows how it works with multiple entries that are printed from the encrypted log file.
![image](https://github.com/alphahunter15/UCSB-CCS-Computing/blob/main/Not_Needed_For_Download/Github.jpg?raw=true)

This image is a screencap of the second encryption method. While the Fernet encryption and decryption is more complicated, this is indicative of the relative complexity of most of the methods I made specifically for this program.
![image](https://github.com/alphahunter15/UCSB-CCS-Computing/blob/main/Not_Needed_For_Download/Github2.jpg?raw=true)
# Installation
For exact steps from opening this repository to complete installation and running the file, go to [this google doc](https://docs.google.com/document/d/1mGp1GLM2mWppr5IwcDUkTvyPte51XdOpkXdlRKzvZXQ/edit?usp=sharing)
# Tests
For a list of possible tests and expected responses see [this google doc](https://docs.google.com/document/d/1eEvCztSxY11deTZfoWER0_cVR8TdM1DOIHUwwQolXHg/edit?usp=sharing)
# How To Use
This is supposed to be used for storing three types of information in three different logs. Although I used the methods for a personal log, a log for college essay ideas, and a log for christmas gift ideas, the uses of this can be expanded to many more logs with different storing functions. This can be used for fun, like how I have used it, or it can be used for storing your deepest, darkest secrets (although this is more of a proof of concept than a finished project so I would wait until version 2.0 comes out).
# Where This Can Be Improved
I could combine all encryption methods into one to create a much more complicated and harder to crack the system. For example, it is easy to see a string is encoded with Fernet encryption becuase each string starts with gAAAAA. Combining methods would get rid of this hint. 
# Contribute
See [Contributions.md](https://github.com/alphahunter15/UCSB-CCS-Computing/blob/main/Not_Needed_For_Download/Contributions.md)
# Credits
My Uncle David, who taught me my first line of code and helped immensely with advising me on how to look professional. 

My parents, who provided their non-computing backround, allowing me to make the system more understandable. 

My sister, who helped me debug my program and gave me many words of encouragement.

[back to top](#ucsb-ccs-computing)
