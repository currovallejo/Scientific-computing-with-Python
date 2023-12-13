class Category:
    
    def __init__(self, category:str):
        self.category = category
        self.ledger = []
    
    def __str__(self):
        a=len(self.category)
        if a%2 == 0:
            line_1 = '*'*((30-a)//2) + self.category + '*'*((30-a)//2) + '\n'
        else:
            line_1 = '*'*((30-a)//2) + self.category + '*'*(((30-a)//2)+1) + '\n'
        line_entries =''
        line_total=''
        total = 0
        for entry in self.ledger:
            description = entry['description']
            number = float(entry['amount'])
            total += number
            number = "{:.2f}".format(number)
            aligned_number = number.rjust(7)
            

            if len(description)>=23:
                description = description[:23]
                len_vacio=0
            else:
                len_vacio = 23-len(description)

            line_entries += description + ' '*(len_vacio) + aligned_number + '\n'           
        
        line_total = 'Total: ' + "{:.2f}".format(total)

        return line_1+line_entries+line_total
    
    def deposit(self, amount, description=""):
        entry = {"amount": amount, "description": description}
        self.ledger.append(entry)
    
    def withdraw(self, amount, description=""):
    
        if self.check_funds(amount)==True:
            self.ledger.append({"amount": -amount, "description": description})
            withdrawal = True
        else:
            withdrawal = False
        
        return withdrawal
    
    def get_balance(self):
        funds = 0
        for entry in self.ledger:
            funds += entry['amount']
        print(funds)
        return funds
    
    def transfer(self, amount, budget_category):
        
        if self.check_funds(amount)==True:
            self.ledger.append({"amount": -amount, "description":'Transfer to ' + str(budget_category.category)})
            budget_category.deposit(amount, 'Transfer from ' + str(self.category))
            transfer =True
        else:
            transfer =False
        
        return transfer
    
    def check_funds(self, amount):
        funds = 0
        for entry in self.ledger:
            funds += entry['amount']
        
        if amount>funds:
            check=False
        else:
            check=True
        
        return check
 
def create_spend_chart(categories):

    bc = 'Percentage spent by category\n'
    withdrawal = []
    percentage_withdrawal = []
    max_len_name=0
    for i,categorie in enumerate(categories):
        print(i)
        print(withdrawal)
        withdrawal.append(0)
        if len(categorie.category) > max_len_name:
            max_len_name = len(categorie.category)
        for dict in categorie.ledger:
            if dict['amount'] < 0:
                withdrawal[i] += - dict['amount']
        print('el withdrawal[i] es: ', withdrawal[i])
        
    total_withdrawal = sum(withdrawal)
    print(total_withdrawal)
    
    for i,j in enumerate(categories):
        percentage_withdrawal.append(withdrawal[i]/total_withdrawal*1000//10)
        print('el percentage_withdrawal para %s es: %s' %(i, percentage_withdrawal[i]))

    for j in range(100,-1,-10):
        if j == 100:
            bc += str(j).rjust(3) + '| '
        else:
            bc += '\n' + str(j).rjust(3) + '| '
        for i,categorie in enumerate(categories):
            if j<=percentage_withdrawal[i]:
                bc += 'o  '
            else:
                bc += '   '
    
    bc += '\n' + '    ' + '---'*len(categories) +'-' + '\n'
    
    for i in range(max_len_name):
        bc += ' '*5
        for j,categorie in enumerate(categories):
            if i<=len(categorie.category)-1:
                bc += categorie.category[i] + ' '*2
            else:
                bc += ' '*3
            if j==len(categories)-1 and i!= max_len_name-1:
                bc += '\n'

    return bc