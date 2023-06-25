#pizza order program
small_pizza = 100
med_pizza = 200
large_pizza = 300
bill = 0
order1 = input("Hello\nWhat kind of pizza would you like?\nsmall, medium or large?")
pepperoni_choice = input("Would you like pepperoni? (y/n): ")
extra_cheese = input("Would you like extra cheese? (y/n): ")
if (order1 == 'small'):
    print("Invoice:")
    print("Small pizza - $100")
    bill = small_pizza
    if (pepperoni_choice == 'y' or pepperoni_choice == 'Y'):
        print("Pepperoni - $30")
        bill = small_pizza + 30
    else:
        bill = small_pizza
    if (extra_cheese == 'y' or extra_cheese == 'Y'):
        print("Extra cheese - $20")
        bill = bill+20
    else:
        bill = bill
elif (order1 == 'medium'):
    print("Invoice:")
    print("Medium pizza - $200")
    bill = med_pizza
    if (pepperoni_choice == 'y' or pepperoni_choice == 'Y'):
        print("Pepperoni - $50")
        bill = med_pizza + 50
    else:
        bill = med_pizza
    if (extra_cheese == 'y' or extra_cheese == 'Y'):
        print("Extra cheese - $20")
        bill = bill + 20
elif (order1 == 'large'):
    print("Invoice:")
    print("Large pizza - $300")
    bill = large_pizza
    if (pepperoni_choice == 'y' or pepperoni_choice == 'Y'):
        print("Pepperoni - $50")
        bill = large_pizza + 50
    else:
        bill = bill
    if (extra_cheese == 'y' or extra_cheese == 'Y'):
        print("Extra cheese - $20")
        bill = bill + 20
    else:
        bill = bill
print(f"Your final total is ${bill}")
