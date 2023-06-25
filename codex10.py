#Love calculator - compare both names to 'TRUE LOVE'
name1 = input("Enter a name: ")
name2 = input("Enter another name: ")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
total_names = lower_name1 + lower_name2
print("Total names: " + total_names)
compare1 = 0 #"TRUE"
compare2 = 0 #"LOVE"

if(total_names.count('t') != 0):
    compare1 += total_names.count('t')

if (total_names.count('r') != 0):
    compare1 += total_names.count('r')

if (total_names.count('u') != 0):
    compare1 += total_names.count('u')

if (total_names.count('e') != 0):
    compare1 += total_names.count('e')


if(total_names.count('l') != 0):
    compare2 += total_names.count('l')

if(total_names.count('o') != 0):
    compare2 += total_names.count('o')

if(total_names.count('v') != 0):
    compare2 += total_names.count('v')

if(total_names.count('e') != 0):
    compare2 += total_names.count('e')

love_calc = str(compare1) + str(compare2)
print("Your love calculator is: " + love_calc + "%")
