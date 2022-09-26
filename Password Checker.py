# Ask username and password from user. 
# Hide password with stars and show lenght of password to user

import time

username = input("Please, write your username: ")
your_password = input("Set a password: ")

password_lenght = len(your_password)
your_passwod_hidden = 'x' * password_lenght

print(f'Hi {username}! Your is password {your_passwod_hidden} and it is {password_lenght} letters long.')

# importing time here to give some break after last answer
time.sleep(3)

# Now trying to ask user if he wants me to show his password
while True: 
    unhidden = input('Please press "Y" to show your password: ')
    if unhidden == "Y":
        print(f'Your password is "{your_password}" ')
        break
    else:
        print("Sorry, you didn't hit 'Y'. I can't show it to you")
  

