#WAP to select a random name from a list of names
# and the person selected will have
# to pay for everybodys bill
import random

#names = input("Enter the names of the friends separated by a comma")
#names_splitted = names.split(",")
names_splitted = ["Jen", "Aak", "Ank", "Payal"]
print(names_splitted)

#length = len(names_splitted)
#payer_index = random.randint(0,length-1)
#print(names_splitted[payer_index)

payer = random.choice(names_splitted)
print(payer)