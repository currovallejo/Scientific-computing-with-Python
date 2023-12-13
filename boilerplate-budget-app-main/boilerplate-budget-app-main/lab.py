import budget

food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")
categories = [ business, food, entertainment]

# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)

# print(budget.create_spend_chart(categories))



food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)

print(food)

print(f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33")

# description = 'esta es '
# number = 7000
# number = "{:.2f}".format(number)
# aligned_number = number.rjust(7)

# if len(description)>=23:
#     description = description[:23]
#     len_vacio=0
# else:
#     len_vacio = 23-len(description)

# vacio = description + ' '*(len_vacio) + aligned_number

# print(vacio)

# antonio = Category('pepino')
# print(antonio)
# antonio.deposit(556.56,'pepinos de mar')
# antonio.deposit(27.58,'pepinos de tierra')
# antonio.withdraw(400, 'hipoteca')
# print(antonio)
# print(antonio.ledger)
# print(antonio.category)

# pepe = Category('Food')
# pepe.deposit(556.56,'pepinos de mar')
# pepe.deposit(27.58,'pepinos de tierra')
# pepe.withdraw(500, 'hipoteca')

# lista=[antonio, pepe]
# print(budget.create_spend_chart(lista))