import random
import string
letters = list(string.ascii_letters)
numbers = list(string.digits)
#symbols = list(string.punctuation)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#print(letters)
#print(numbers)
#print(symbols)
print("Welcome to the password generator!")
n_letters=4 #int(input("How many letter do you want? "))
n_numbers=4 #int(input("How many numbers do you want? "))
n_symbols=4 #int(input("How many symbols do you want? "))

rand_letter = ''
rand_number = ''
rand_symbol = ''

for i in range(0,n_letters): #Generate random letters
    rand_letter += random.choice(letters)

print(rand_letter)

for i in range(0,n_numbers): #Generate random numbers
    rand_number += random.choice(numbers)

print(rand_number)

for i in range(0,n_symbols): #Generate random symbols
    rand_symbol+= random.choice(symbols)

print(rand_symbol)

pw = rand_letter + rand_number + rand_symbol
print(pw)
#print(type(pw))
pw_random = list(pw)
print(pw_random)
random.shuffle(pw_random)
print (''.join(pw_random))
#random.shuffle(pw)
#print(pw)