class Initial:
    choice_opt = [
        "", 
        "********** Bank Management System **********", 
        "1. Create a new Account", 
        "2. Deposit Money",
        "3. Withdraw Money", 
        "4. Check Balance", 
        "5. Exit", 
        ""
    ]
    
    @staticmethod
    def options():
        for each_opt in Initial.choice_opt:
            print(f"{each_opt}")

class DataStored:
    stored = []  # Holds account data 


class DataFromUser:

    @staticmethod
    def create_acc(acc_name, acc_no, set_pass, ammount):
        DataStored.stored.append([acc_name, acc_no, set_pass, ammount])
        print("\n'Congratulation', Account created successfully")

    @staticmethod
    def deposit(acc_no, password):
        for account in DataStored.stored:
            # Check account number and password
            if account[1] == acc_no and account[2] == password:  
                depo_bl = float(input(">> How much do you want to deposit: "))
                if depo_bl < 500:
                    print("\nError << Minimum deposit is 500 TK.")
                elif depo_bl <= 0:
                    print("\nError << Deposit balance cannot be negative or zero.")
                else:
                    account[3] += depo_bl
                    print("\nYour deposit was successful!")
                return
        
        print("\nError << Account does not exist or incorrect password.")


    @staticmethod
    def withdraw(acc_no, password):
        for account in DataStored.stored:
            # Check account number and password
            if account[1] == acc_no and account[2] == password: 
                withdraw_bl = float(input(">> How much do you want to withdraw: "))
                if withdraw_bl <= 0:
                    print("\nError << Withdrawal amount must be greater than zero.")
                elif withdraw_bl > account[3]:
                    print("\nError << Insufficient balance.")
                else:
                    account[3] -= withdraw_bl
                    print("\nYour withdrawal was successful!")
            else:        
                print("\nError << Account does not exist or incorrect password.")
                return

    @staticmethod
    def check_balance(acc_no):
        # Find account by account number
        for account in DataStored.stored:
            if account[1] == acc_no:
                print(f"\nYour current balance: {account[3]} TK")
        
            else:
                print("\nError << Account does not exist.")
                return


class Banking:

    while True:
        Initial.options()
        choice = input("\n>> Enter your choice number (1-5): ")

        if choice == "1":
            acc_name = input("\n>> Enter your identity: ")
            acc_no = int(input(">> Enter the account number: "))
            password = input(">> Enter the password of your account: ")
            initial_balance = float(input(">> Enter initial deposit amount (minimum 500 TK): "))

            if initial_balance < 500:
                print("\nError << Initial deposit must be at least 500 TK.")
            else:
                DataFromUser.create_acc(acc_name, acc_no, password, initial_balance)

        elif choice == "2":
            acc_no = int(input("\n>> Enter the account number: "))
            password = input(">> Enter the password of your account: ")
            DataFromUser.deposit(acc_no, password)

        elif choice == "3":
            acc_no = int(input("\n>> Enter the account number: "))
            password = input(">> Enter the password of your account: ")
            DataFromUser.withdraw(acc_no, password)

        elif choice == "4":
            acc_no = int(input("\n>> Enter the account number: "))
            DataFromUser.check_balance(acc_no)

        elif choice == "5":
            print("\nThanks for using the Bank Management System!")
            break
        
        else:
            print("\nError << Invalid choice, please enter a valid number.")
