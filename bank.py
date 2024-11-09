# Bank management process
choice_options = [
    "", "********** Bank Management System **********", "", "1. Create Account", "2. Deposit Money",
    "3. Withdraw Money", "4. Check Balance", "5. Check information of your account ", "6. Account delete", "7. Exit"
]
for option in choice_options:
    print(option)

# All information is stored here
accounts = {}


# Operations of new accounts
def create_account():
    print("\n----- Create a new account -----")
    ac_name = input(">> Enter your Identity : ")
    if " " == (ac_name):
        return "\nError << Please type your original or valid name ....."
    else:
        user_name = input(">> Enter the username : ")
        if (2 >= len(user_name)) or (len(user_name) > 15):
            return "\nError << User name at least 4 to 10 characters....."
        else:
            age = float(input(">> Enter your current age : "))
            if (0 > age) or (age < 18):
                return "\nError << Error << Must be 18 years old or above....."
            else:
                acc_num = input(">> Enter the account number (must be 12 digits) : ")
                if (len(acc_num) != 12) or (" " == (acc_num)):
                    return "\nError << Account number must be 12 digits and unique number....."
                else:
                    acc_pass = input(">> Enter the New password(strong) : ")
                    if acc_pass is "":
                        return "\nError << Please setup Strong Password for your Bank account....."
                    else:
                        deposit = float(input(">> How much do you want to invest : "))
                        if (deposit < 500) or (deposit < 0):
                            return "\nError << Deposit balance must be not-nagative and Minimum deposit 500 TK....."
                        else:
                            accounts.update(
                                {ac_name: {
                                    "User Name": user_name,
                                    "Age": age,
                                    "Account number": acc_num,
                                    "Password": acc_pass,
                                    "Total balance": deposit
                                }})
                            return "\n'Congratulation', Account created successfully"


# Operations of Deposit sytem
def deposit_part():
    for keys, value in accounts.items():
        key = keys
    try:
        print("\n--- Investment part of the bank ---")
        ac_name = input(">> Enter your Identity : ")
        if (3 > len(ac_name) or len(ac_name) > 15):
            return "\nError << Account name at least 5 to 10 characters....."
        else:
            acc_num = input(">> Enter the account number (must be 12 digits) : ")
            if len(acc_num) != 12:
                return "\nError << Account number must be 12 digits....."
            else:
                acc_pass = input(">> Enter the account password : ")
                if acc_pass is None:
                    return "\nError << Please setup Strong Password for your Bank account....."
                else:
                    deposit = float(input(">> How much do you want to invest : "))
                    if (deposit < 500) or (deposit < 0):
                        return "\nError << Deposit balance must be not-nagative and Minimum deposit 500 TK....."
                    else:
                        if (accounts[ac_name]) != (accounts[key]):
                            return "\nError << Account does not exist. please Create a new account....."
                        else:
                            if (accounts[key]["Account number"]) != (acc_num):
                                return "\nError << Account does not exist, becuse account number does't match....."
                            else:
                                if (accounts[key]["Password"]) != (acc_pass):
                                    return "\nError << Sorry, Password does't matched in your account....."
                                else:
                                    accounts[key]["Total balance"] += deposit
                                    return '\nYour Deposit Successfully.'

    except KeyError:
        return "\nError << Account does not exist. please Create a new account....."


# Operations of withraw part
def withraw_money():
    for keys, value in accounts.items():
        key = keys
    try:
        print("\n---- Withdraw section ----")
        ac_name = input(">> Enter your account name or Identity : ")
        if (key) != (ac_name):
            return "\nError << Account name does not matched, Type same name of your account name......"
        else:
            acc_num = input(">> Enter the account number (must be 12 digits) : ")
            if (accounts[key]["Account number"]) != (acc_num):
                return "\nError << Account number does not matched, please try again"
            else:
                acc_pass = input(">> Enter the account password : ")
                if (accounts[key]["Password"]) != (acc_pass):
                    return "\nError << Sorry, Password does not matched....."
                else:
                    withdraw_money = float(input(">> How much do you want to withdraw : "))
                    if (accounts[key]["Total balance"]) < (withdraw_money):
                        return "\nError << Insufficient Balance for Withdrawal, your current balance : ", accounts[key][
                            "Total balance"]
                    else:
                        accounts[key]["Total balance"] = accounts[key]["Total balance"] - withdraw_money
                        return "Your withraw process successfully, your current balance in your account : ", \
                        accounts[key]["Total balance"]
    except:
        return "\nError << Account does not exist, please create a new account."


# Operation of balance inquiry
def check_balance():
    for keys, value in accounts.items():
        key = keys
    try:
        print("\n----- Balance Inquiry -----")
        ac_name = input(">> Enter your account name or Identity : ")
        if (key) != (ac_name):
            return "\nError << Account name does not matched, try again or Create a new account....."
        else:
            acc_num = input(">> Enter the account number (must be 12 digits) : ")
            if (accounts[key]["Account number"]) != (acc_num):
                return "\nError << Account number does not matched, please try again....."
            else:
                acc_pass = input(">> Enter the account password : ")
                if (accounts[key]["Password"]) != (acc_pass):
                    return "\nError << Sorry, Password does not matched....."
                else:
                    return "Your current balance : ", accounts[key]["Total balance"]
    except:
        return "\nError << Account does not exist, please create a new account."


# Information check of bank account
def check_info():
    for keys, value in accounts.items():
        key = keys
    try:
        print("\n---- Check your bank informations ----")
        ac_name = input(">> Enter your account name or Identity : ")
        if (key) != (ac_name):
            return "\nError << Account name does not matched, Type same name of your account name......"
        else:
            acc_num = input(">> Enter the account number (must be 12 digits) : ")
            if (accounts[key]["Account number"]) != (acc_num):
                return "\nError << Account number does not matched, please try again"
            else:
                acc_pass = input(">> Enter the account password : ")
                if (accounts[key]["Password"]) != (acc_pass):
                    return "\nError << Sorry, Password does not matched....."
                else:
                    return "\nAll your Information -- ", accounts[key]
    except:
        return "\nError << Account does not exist, please create a new account.."


# section of Delete acconts
def acc_delete():
    for keys, value in accounts.items():
        key = keys
    try:
        print("\n-- Enter the info to delete your account --")
        ac_name = input(">> Enter your account name or Identity for Account delete : ")
        if (key) != (ac_name):
            return "\nError << Account name does not matched, Type same name of your account name......"
        else:
            acc_num = input(">> Enter the account number (must be 12 digits) : ")
            if (accounts[key]["Account number"]) != (acc_num):
                return "\nError << Account number does not matched, please try again"
            else:
                acc_pass = input(">> Enter the account password : ")
                if (accounts[key]["Password"]) != (acc_pass):
                    return "\nError << Sorry, Password does not matched....."
                else:
                    accounts[key].clear()
                    return "\nYour Account has been deleted successfully."
    except:
        return "\nError << Account does not exist, please create a new account.."


while True:
    choice = input("\n >> Ente your choice Number (1/7): ")
    if choice == "1":
        print(create_account())

    elif choice == "2":
        print(deposit_part())

    elif choice == "3":
        print(withraw_money())

    elif choice == "4":
        print(check_balance())

    elif choice == "5":
        print(check_info())

    elif choice == "6":
        print(acc_delete())
    elif choice == "7":
        print("\nThank you")
        print()
        break
    else:
        print("\nError << 'Type valid choice option'.....")




