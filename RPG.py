# mod
import string
import random


# def
def save_password_to_file():
    file = open("password.txt", "w")
    for temp in password:
        file.write(temp)
    file.close()


print("Hello to Random Password Generator! ")

# length password
length_password = int(input('Enter the length of yours password: '))
if length_password >= 95:
    print("Too long password")
if length_password <= 0:
    print("Invalid length")
    exit()

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
letters = string.ascii_letters

# combine the data
all = lower + upper + num + symbols + letters

# use random
temp = random.sample(all, length_password)

# create password
password = "".join(temp)

# print
print("Your's new password =" + " " + password)
print("Good password ;)")
save_password_to_file()


