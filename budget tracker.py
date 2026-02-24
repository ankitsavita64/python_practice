from datetime import datetime

print("#"*20,"welcome to your budget tracker","#"*20)

income=float(input("enter your monthly income here :$"))
expenses={}
expenses_amount=0

while True:
    item=input("\n enter expenses name (or type 'done' to finish):").lower()

    if item =='done':
        break

    try:
        amount=float(input(f"how much did {item} cost? $"))
        expenses[item]=amount
        expenses_amount += amount
        print(f"current total spent:${expenses_amount}")
    
    except ValueError:
        print("invalid price! please enter a number.")

remaining=income-expenses_amount

if remaining>=0:
    print(f"great job! you have ${remaining} left")
else:
    print(f"warning! you are over budget by ${remaining}.")

print("\n---detalis of total expenses---")
for name,cost in expenses.items():
    print(f"{name.capitalize()} : ${cost}")

# for print summary of expenses.
print("\n---FINAL BUDGET SUMMARY---")
print(f"your initial budget:${income}")
print(f"total spent:${expenses_amount}")
percentage = (expenses_amount / income) * 100
print(f"You spent {percentage:.2f}% of your income.")

# for store data you create into a file 
with open("expenses.txt", "a+") as file:
    file.write(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
    file.write(f"Monthly Income: ${income}\n")
    file.write("Expenses:\n")
    for name, cost in expenses.items():
        file.write(f"{name} : ${cost}\n")
    file.write(f"\nTotal Spent: ${expenses_amount}\n")
    file.write(f"Remaining Budget: ${remaining}\n")

print("Data saved successfully in expenses.txt")

'''def monthly_report(income, spent):
    remaining = income - spent
    print("\n----- MONTHLY REPORT -----")
    rint(f"Income: ${income}")
    print(f"Total Spent: ${spent}")
    print(f"Remaining: ${remaining}")'''

# for set password to secure file(expenses.txt).
'''print("Do you want to set a password?")
choice = input("Type 'yes' to set password or 'no' to skip: ").lower()

if choice == "yes":
    saved_password = input("Set your password: ")
    
    entered_password = input("Enter password to access Budget Tracker: ")
    
    if entered_password != saved_password:
        print("Access Denied.")
        exit()
    else:
        print("Access Granted.")

elif choice == "no":
    print("No password set. Continuing...")

else:
    print("Invalid choice. Program exiting.")
    exit()'''