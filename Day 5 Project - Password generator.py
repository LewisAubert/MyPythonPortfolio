#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = "" #this step is saying that as it stands, our string for our password is empty.
# #nr_letters = 4
# for char in range(1, nr_letters + 1): #we add 1 every time because if we did not, we would get a range from 1-3, and not 1-4. Python does not count the final number.
#   password += random.choice(letters) #we are updating the password variable every time.

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# print(password)

#issue with a password like this is that there is not random order of letters, numbers and symbols. It is easy to crack. We want a random order. Instead of using a password string, we will use a password list.

password_list = []

for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

# print(password_list) #get rid of this line
random.shuffle(password_list)
# print(password_list) #this needs to be turned back into a string. The .shuffle() function does what it says. It shuffles the order. I will also get rid of this line.

password = ""
for char in password_list:
  password += char

print(f"Your password is {password}")