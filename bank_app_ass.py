# import random
# import time
# from datetime import datetime


# def deposit(amount: float, prev_balance: float):
#     new_bal = amount + prev_balance
#     return new_bal


# def withdrawal(amount: float, prev_balance: float):
#     if (amount > prev_balance):
#         raise ValueError("Insufficient Funds")
#     else:
#         new_bal = prev_balance - amount
#     return new_bal


# def account_number():
#     acct_no = "0"
#     for i in range(9):
#         acct_no += str(random.choice(range(10)))
#     return acct_no


# data = {}

# print("Welcome to the Bitcoin Core")
# while True:
#     print("What would you like to do?\n1. Create a new account.\n2. Login to an existing account.\n3. Quit.")
#     user_input = input('::>>')

#     if (user_input == '1'):
#         first_name = input('First Name:\n>')
#         last_name = input('Last Name:\n>')
#         pin = input('Login Pin:\n>')
#         trans_pin = input('Transaction Pin:\n>')
#         acc_num = account_number()
#         print("Account creation processing...")
#         time.sleep(3)
#         print('Successful')
#         time.sleep(2)

#         data[acc_num] = {
#             'name': f"{first_name} {last_name}",
#             'pin': pin,
#             'trans_pin': trans_pin,
#             'bal': 0,
#         }

#         print(f"""\nWelcome, {first_name} {last_name}!
# You have successfully created your account on the bitcoin core. Your account number is {acc_num}.
# Please keep your pin safe from scammers.
# Cheers,
# Coache.
# (CEO Bitcoin Core)""")

#     elif (user_input == "2"):
#         acc_num = input("Account Number:> ")
#         pin = input("LoginPin:> ")

#         user_data = data.get(acc_num)

#         if user_data and user_data.get("pin") == pin:
#             print("Login Successful")
#             first_login = True
#             while True:
#                 if first_login:
#                     print(
#                         f"Welcome, {user_data['name'].split()[0].capitalize()}")
#                     first_login = False
#                 else:
#                     print(
#                         f"Welcome back, {user_data['name'].split()[0].capitalize()}")

#                 print(
#                     "What would you like to do? \n1. Withdrawal \n2. Deposit \n3. Transfer \n4. Check Balance \n5. Logout")
#                 input_ = input(":> ")
#                 if (input_ == "1"):
#                     amount = float(input("Amount: \n>"))
#                     try:
#                         new_bal = withdrawal(amount, user_data["bal"])
#                         user_data["bal"] = new_bal
#                     except ValueError as message:
#                         print(message)

#                 elif (input_ == "2"):
#                     amount = float(input(""))
#                     trans_pin = input("Transaction Pin:\n>")
#                     if trans_pin == user_data['trans_pin']:
#                         amt = deposit(amount, user_data['bal'])
#                         user_data['bal'] = amt
#                     else:
#                         print("Invalid pin value")

#                 elif (input_ == "3"):
#                     other_acc = input("Enter Account number\n:>> ")
#                     trans_amount = int(
#                         input("Enter Amount you want to Transfer\n:>> "))
#                     trans_pin = input("Enter transaction pin:\n>")

#                     beneficiary = data.get(other_acc)
#                     if beneficiary:
#                         if trans_amount > user_data['bal']:
#                             print("Insufficient Funds")
#                         else:
#                             if trans_pin == user_data['trans_pin']:
#                                 user_data['bal'] -= trans_amount
#                                 beneficiary['bal'] += trans_amount
#                                 print("\nTransfer Successful")
#                             else:
#                                 print("Incorrect pin.")

#                 elif (input_ == "4"):
#                     current_date = datetime.now().date()
#                     date = current_date.strftime("%a, %d of %B, %Y")
#                     print(
#                         f"Your current balance at {date} is {user_data['bal']}")

#                 elif input_ == "5":
#                     break
#         else:
#             print("Invalid Credential.")
#     elif (user_input == "3"):
#         break

# print("\n", data)


from distutils.command.build_scripts import first_line_re
import time
import random


def account_number():
    number = "0"
    for items in range(9):
        number += str(random.choice(range(10)))
    return number


def withdrawal(amount, prev_bal):
    if (amount > prev_bal):
        raise ValueError("Insufficient funds")
    else:
        current_bal = prev_bal - amount
    return current_bal


def deposit(amount, prev_bal):
    current_bal = amount + prev_bal
    return current_bal


bank = {}


while True:
    print("Welcome to Easy Online Bank")
    print("""What would you like to do?
      1. Type "1" to create an account.
      2. Type "2" to Login.
      3. Type "3" to Quit. """)

    user_input = input(":> ")
    if(user_input == "1"):
        first_name = input("Enter your first name:> ").lower()
        last_name = input("Enter your last name:> ").lower()
        pin = (input("Enter a four-digit pin:> "))
        trans_pin = (input("Enter a four-digit transaction pin:> "))
        account_no = account_number()
        print("Processing...")
        time.sleep(3)
        print("successful")
        time.sleep(2)

        bank[account_no] = {"name": "f{first_name} {last_name}",
                            "pin": pin,
                            "trans_pin": trans_pin,
                            "balance": 0
                            }
        print(
            f"""Congratulation {first_name.capitalize()} {last_name.capitalize()},
            you have successfully created an account. 
            Your account number is {account_no}, your pin is {pin} and
            your transaction pin is {trans_pin}.""")

    elif (user_input == "2"):
        user_details = bank.get(account_no)
        acc_no = input("Enter your account number:> ")
        user_pin = input("Enter your 4-digit pin:> ")

        if(user_details and user_details["pin"] == user_pin):
            print("Login Successful ")
            print("""What would you like to do?
      1. Type "1" to deposit.
      2. Type "2" to Withdraw.
      3. Type "3" to Transfer.
      4. Type "4" to Check-Balance.
      5. Type "5" to Logout. """)

        else:
            print("Wrong Login details")

        break
