import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="bank"
)
cursor = db.cursor()

def create_account(name, balance, account_type):
    sql = "INSERT INTO accounts (name, balance, account_type) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, balance, account_type))
    db.commit()
    print("Account created successfully!")

def deposit(account_id, amount):
    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id,))
    current_balance = cursor.fetchone()[0]
    new_balance = current_balance + amount
    cursor.execute("UPDATE accounts SET balance = %s WHERE id = %s", (new_balance, account_id))
    db.commit()
    print("Deposit successful. New balance:", new_balance)

def withdraw(account_id, amount):
    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id,))
    current_balance = cursor.fetchone()[0]
    if current_balance >= amount:
        new_balance = current_balance - amount
        cursor.execute("UPDATE accounts SET balance = %s WHERE id = %s", (new_balance, account_id))
        db.commit()
        print("Withdrawal successful. New balance:", new_balance)
    else:
        print("Insufficient balance!")

def check_balance(account_id):
    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id,))
    balance = cursor.fetchone()[0]
    print("Your balance is:", balance)

def show_number_of_accounts():
    cursor.execute("SELECT COUNT(*) FROM accounts")
    num_accounts = cursor.fetchone()[0]
    print("Number of accounts:", num_accounts)

def show_number_of_users():
    cursor.execute("SELECT COUNT(DISTINCT name) FROM accounts")
    num_users = cursor.fetchone()[0]
    print("Number of users:", num_users)

def choose_account_type(account_id, account_type):
    cursor.execute("UPDATE accounts SET account_type = %s WHERE id = %s", (account_type, account_id))
    db.commit()
    print("Account type updated successfully.")

def show_card_type(account_id):
    cursor.execute("SELECT account_type FROM accounts WHERE id = %s", (account_id,))
    card_type = cursor.fetchone()[0]
    if card_type=="debit":
        print("User uses Debit Card.")
    elif card_type=="credit":
        print("User uses Credit Card.")
    elif card_type=="both":
        print("User uses both Debit and Credit Card.")
    else:
        print("User has not chosen any card type.")
def loan(income,loanamount):
    if income<300000:
        check_balance=check_balance+0
        print("Loan can't be granted to you ")
    elif income>500000:
        check_balance=check_balance+(loanamount/2)
        print("Yoyr Loan is granted But upto 50% due to low income and low credit score")
    elif income>10000000:
        print("Loan Granted ")
    else:
        print("No Loan can't be granted ")
        

def main():
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Show Number of Accounts")
        print("6. Show Number of Users")
        print("7. Choose Account Type")
        print("8. Show Card Type")
        print("9.Loan")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            account_type = input("Choose account type (debit, credit, or both): ")
            create_account(name, initial_balance, account_type)
        elif choice == "2":
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to deposit: "))
            deposit(account_id, amount)
        elif choice == "3":
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to withdraw: "))
            withdraw(account_id, amount)
        elif choice == "4":
            account_id = int(input("Enter account ID: "))
            check_balance(account_id)
        elif choice == "5":
            show_number_of_accounts()
        elif choice == "6":
            show_number_of_users()
        elif choice == "7":
            account_id = int(input("Enter account ID: "))
            account_type = input("Choose account type (debit, credit, or both): ")
            choose_account_type(account_id, account_type)
        elif choice == "8":
            account_id = int(input("Enter account ID: "))
            show_card_type(account_id)
        elif choice =="9":
            income=float(input("Enter your annual income"))
            loanamount=float(input("enter the Loan amount you want "))
            loan(income,loanamount)
        elif choice == "10":
            print("Thank you for using our services!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
