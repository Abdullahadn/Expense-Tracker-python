import datetime

# Class to represent single Expense record.
class Expense:
    def __init__ (self,category,amount,date,note = "This is a product"):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

# Class to manage and track multiple expenses.        
class ExpenseTracker:
    
    def __init__ (self):
        self.expenses_list = []    
           
    def add_expense(self,category,amount,date,note):
        expense = Expense(category,amount,date,note)
        self.expenses_list.append(expense) 
          
          
    def delete_expense(self,index):
        if 0<= index < len(self.expenses_list): 
            del self.expenses_list[index]  
            print("\nExpense Deleted!") 
        else: print("Invalid Item Number!")
          
    def update_expense(self,index):
        if 0<= index < len(self.expenses_list):
            update = int(input("\n1.Category\n2.amount\n3.date\n4.note\nEnter the attribute to Update: "))
            if (update ==1): self.expenses_list[index].category = choose_category()
            elif (update ==2): self.expenses_list[index].amount = float(input('Enter Updated amount: '))
            elif(update == 3): self.expenses_list[index].date = choose_date()
            elif(update ==4): self.expenses_list[index].note= (input("Enter Updated Note: "))
            else: print("Wrong Index Chosen!")
        else: print ("Invalid item Number!")
    
    def total_expense(self):
        total = 0
        for expense in self.expenses_list:
            total = total + expense.amount
        return total  
          
    def display_expense(self):
        i = 1
        for expense in self.expenses_list:
            print("-" * 10,"\nITEM",i,"\n1.Category : ",expense.category,"\n2.Amount :",expense.amount,"\n3.Date : ",expense.date,"\n4.Note : ",expense.note)
            i= i+1
    def filter_by_date(self,date):
        day_total = 0
        for expense in self.expenses_list:
            if(date == expense.date):
                print(f"Category: {expense.category} , Amount: {expense.amount}, Date: {expense.date}, Note: {expense.note} ")       
                day_total = day_total + expense.amount
        if (day_total == 0): print("No entries for ", date)
        print("Total for ", date,": ",day_total)
    
    def filter_by_month(self,month):
        month_total = 0
        for expense in self.expenses_list:
            if(month == expense.date.month):
                print(f"Category: {expense.category} , Amount: {expense.amount}, Date: {expense.date}, Note: {expense.note} ")       
                month_total = month_total + expense.amount
        if (month_total == 0): print("No entries for ", month)
        print ("Total for ",month,": ", month_total)
    
    def filter_by_category(self,category):
        category_total = 0
        for expense in self.expenses_list:
            if(category == expense.category):
                print(f"Category: {expense.category} , Amount: {expense.amount}, Date: {expense.date}, Note: {expense.note} ")       
                category_total = category_total + expense.amount
        if (category_total == 0): print("No entries for ", category)
        print ("Total for ",category,": ", category_total)
     
# Functions Outside the class

# Function to allow user to select a category from predefined option       
def choose_category():
    while True:
        category_dict = {1:'Food',2:'Transport',3:'Shopping',4:'Utilities',5:'Entertainment',6:'Health',7:'Education'}
        try:
            key = int(input("\nSELECT CATEGORY \n1.Food\n2.Transport\n3.Shopping\n4.Utilities\n5.Entertainment\n6.Health\n7.Education\n\nEnter Choice: "))
            if key not in category_dict.keys():
                print("Invalid Category Chosen")
                continue
            return category_dict[key]
        except ValueError : print("Invalid Input!")
 
# Function to prompt user to input a valid date   
def choose_date():
    while True:
        try:
            
            month = int(input("\nEnter Date\nMonth(1-12): "))
            day = int(input("Day(1-31): "))
            year = int(input("Year(e.g. 2025): "))
            date = datetime.datetime(year,month,day).date()
        except ValueError:
            print("Invalid Input\n")
            continue
        break
    return date
 
# Password verification to restrict access to sensitive actions: Add, Delete, Update   
def verify():
    password = 'manager-123'
    while (True):
        enter = input("\nEnter Password: ")
        if (enter != password):
            print("Try again!")
            continue
        print("Correct Password!")
        break
    
    
# Main program loop
tracker = ExpenseTracker()
print("\n\t\t\t\tWELCOME TO EXPENSE TRACKER")

while True:
    # Display menu options for user
    print("-" * 30,"\n1.Add Expense\n2.Delete Expense\n3.Update Expense\n4.Filter By Category \n5.Filter By Month\n6.Filter By Date\n7. Display Summary\n8.Exit Program")
    choice = int(input("\nEnter Choice: "))
    try:
        if (choice == 1):
            verify()
            category = choose_category()
            date = choose_date()
            while True: 
                try:
                    amount = float(input("\nEnter Amount: "))
                    note = (input("\nEnter a Note: "))
                    break
                except ValueError: print("Invalid Input")
            tracker.add_expense(category,amount,date,note)
                
        elif (choice == 2):
            verify()
            tracker.display_expense()
            while True:
                try:
                    index = int(input("Enter Item no. of Expense to delete: "))
                    tracker.delete_expense(index-1)
                    break
                except ValueError : print("Invalid Input")
    
        elif (choice == 3):
            verify()
            tracker.display_expense()
            while True:
                try:
                    index = int(input("Enter Item no. of Expense to update: "))
                    tracker.update_expense(index-1)
                    break
                except ValueError : print("Invalid Input")
    
        elif (choice == 4):
            category = choose_category()
            tracker.filter_by_category(category)
        
        elif (choice == 5):
            month = int(input("Month(1-12): "))
            tracker.filter_by_month(month)
        
        elif(choice == 6):
            date = choose_date()
            tracker.filter_by_date(date)
    
        elif (choice == 7):
            print("DISPLAYING SUMMARY")
            tracker.display_expense()
            total = tracker.total_expense()
            print("-"*10,"Total Expenses: ",total)
    
        elif (choice == 8):
            print("Program terminated!")
            break
     
        else: print("Wrong Input \n Try Again!")
    except ValueError:
        print("Invalid Choice!")
        continue
      
print("GOODBYE!")