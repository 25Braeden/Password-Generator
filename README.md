This program will either generate a password or, take your email along with website that the password is for, and save them along with the generated password in a file on your computer so you can remember them.

I have no access to any data that you enter into this program.

The passwords will be automatically saved in the 'dist' folder and the txt file will be called "passwords". If you wish to change anything about this go to lines 48-49

I cannot recommend that this be used for any professional or personal applications as I opted to use the 'random' module instead of the 'secret' module so passwords could be more secure.

If you wish to make the generated passwords more secure go into the code and change these things:

import random --> import secret

(line 43) PASSWORD = ''.join(random.choice(ALPHABET) for i in range (length)) --> 
PASSWORD = ''.join(secret.choice(ALPHABET) for i in range (length))

Repeat the above step for line 70 aswell to make your passwords more secure.

Thanks for using the program!