import os
import random
import time
import platform
import make_database
import getpass
from datetime import datetime

digits = [0,1,2,3,4,5,6,7,8,9]

def clear_terminal():
    if 'Windows' in platform.uname():
        os.system('cls')
    else:
        os.system('clear')

def generate_account_id():
    account_id = ''
    
    while True:
        account_id += str(random.choice(digits))
        if len(account_id)==10:
            break
    return account_id

def generate_account_pin():
    account_pin = ''
    while True:
        account_pin += str(random.choice(digits))
        if len(account_pin) == 5:
            break
    return account_pin

def change_account_pin(account_id):
    new_pin = getpass.getpass("Enter your new 5 digit pin here: ")
    old_pin = make_database.select_account_pin(account_id)
    if new_pin != old_pin:
        if not new_pin.isdigit():
            print("Pin must be made of digits only")
            time.sleep(5)
            clear_terminal()
        elif len(new_pin) != 5:
            print("Pin must be exactly 5 digits long")
            time.sleep(5)
            clear_terminal()
            menu(account_id)
        else:
            #print("You have successfully updated your pin")
            make_database.update_accounts_pin(new_pin,account_id)
            print("\nYou have successfully changed your account pin")
            continue_or_not = input("\n\nEnter E to exit or any other button to return to the main menu: ")
            if continue_or_not == 'E' or continue_or_not == 'e':
                time.sleep(3)
                clear_terminal()
                print("\nExiting program...")
                time.sleep(5)
                clear_terminal()
            else:
                time.sleep(3)
                clear_terminal()
                menu(account_id)
    else:
        print("New pin must be different from the old pin")
        continue_or_not = input("\n\nEnter E to exit or any other button to return to the main menu: ")
        if continue_or_not == 'E' or continue_or_not == 'e':
            time.sleep(3)
            clear_terminal()
            print("\nExiting program...")
            time.sleep(5)
            clear_terminal()
        else:
            time.sleep(3)
            clear_terminal()
            menu(account_id)

def delete_profile(userID,accountID):
    print("\nThis action will delete all of your information from our database, including your bank account")
    choice = input("Are your certain you want to go ahead with this action?[Type Y for yes or N for No]: ")
    if choice == 'Y' or choice == 'y':
        make_database.delete_clients(userID)
        make_database.delete_accounts_all(userID)
        make_database.delete_transactions_single_account_all(accountID)
        time.sleep(5)
        clear_terminal()
        print("\nDeleting profile...")
        time.sleep(5)
        clear_terminal()
        print("\nYou have successfuly deleted your profile.")
        time.sleep(5)
        clear_terminal()
    elif choice == 'N' or choice == 'n':
        time.sleep(5)
        clear_terminal()
        menu(accountID)
    else:
        print(f"{choice} is an invalid choice. Type 'Y' for yes or 'N' for no")
        time.sleep(5)
        clear_terminal()
        menu(accountID)

def user_name_verification(username):
    all_usernames_in_database = make_database.select_all_client_id()
    if username in all_usernames_in_database:
        return False
    else:
        return True

def sign_up():
    credential_list = []
    id = input("Enter your username here: ")
    if id:
        if user_name_verification(id) == True:
            credential_list.append(id)
            password = getpass.getpass("Enter your password here: ")
        else:
            print(f"\n{id} is already taken. Select a new username")
            continue_or_not = input("Enter E to exit or any other button to return to the menu: ")
            if continue_or_not == 'E' or continue_or_not == 'e':
                time.sleep(3)
                clear_terminal()
                print("\nExiting program...")
                time.sleep(5)
                clear_terminal()
            else:
                time.sleep(3)
                clear_terminal()
                sign_up()
        if password:
            credential_list.append(password)
            first_name = input("Enter your first name here: ")
            if first_name:
                credential_list.append(first_name)
                surname = input("Enter your surname here: ")
                if surname:
                    credential_list.append(surname)
                    email = input("Enter your email here: ")
                    if email:
                        credential_list.append(email)
                        # continue_or_not = input("Enter Y to continue or E to exit: ")
                        # if continue_or_not == 'E' or continue_or_not == 'e':
                        #     time.sleep(3)
                        #     clear_terminal()
                    else:
                        print("An email is required.\n")
                        time.sleep(5)
                        clear_terminal()
                        sign_up()
                else:
                    print("A surname is required.\n")
                    time.sleep(5)
                    clear_terminal()
                    sign_up()
            else:
                print("A password is required.\n")
                time.sleep(5)
                clear_terminal()
                sign_up()
        else:
            print("A password is required.\n")
            time.sleep(5)
            clear_terminal()
            sign_up()
    else:
        print("A username is required.\n")
        time.sleep(5)
        clear_terminal()
        sign_up()
    
    account_pin = generate_account_pin()
    account_id = generate_account_id()
    credential_list.append(account_id)
    credential_list.append(account_pin)
    return tuple(credential_list)

def sign_in():
    user_id = input("Enter your username here: ")
    user_password = getpass.getpass("Enter your password here: ")
    if user_name_verification(user_id) == False and (user_password == make_database.select_client_password(user_id)):
            account_id = make_database.select_account_id(user_id)
            return account_id
    else:
        print("Username or password does not match database records")
        continue_or_not = input("Enter E to exit or any other button to return to the landing page: ")
        if continue_or_not == 'E' or continue_or_not == 'e':
            time.sleep(3)
            clear_terminal()
            print("\nExiting program...")
            time.sleep(5)
            clear_terminal()
        else:
            time.sleep(3)
            clear_terminal()
            landing_screen()

def landing_screen():
    print("Select the number associated with action you wish to complete:")
    print("1. Create an account")
    print("2. Login to an account")
    user_choice = input("Enter your choice {1 or 2} here: ")
    if user_choice == '1' or user_choice == '2':
        time.sleep(3)
        clear_terminal()
        return user_choice
    else:
        print("Invalid input, choice must be either 1 or 2")
        time.sleep(5)
        clear_terminal()
        landing_screen()

def check_balance(account_id):
    balance = make_database.select_account_balance(account_id)
    print(f"Your account balance is R {balance}.")
    continue_or_not = input("\n\nEnter E to exit or any other button to return to the main menu: ")
    if continue_or_not == 'E' or continue_or_not == 'e':
        time.sleep(3)
        clear_terminal()
    else:
        time.sleep(3)
        clear_terminal()
        menu(account_id)

def make_deposit(account_id):
    transaction_type = 'cash deposit'
    transaction_amount = input("Enter the deposit amount here: ")
    if transaction_amount.isdigit():
        transaction_amount = int(transaction_amount)
        time_of_transaction = str(datetime.now())
        make_database.insert_into_transactions(account_id,transaction_type,transaction_amount,time_of_transaction)
        make_database.update_accounts_balance_deposit(transaction_amount,account_id)
        new_balance = make_database.select_account_balance(account_id)
        print(f"\nYou have successfully made a R {transaction_amount} cash deposit.\nYour account balance is now {new_balance}")
        continue_or_not = input("Enter E to exit or any other button to return to the main menu: ")
        if continue_or_not == 'E' or continue_or_not == 'e':
            time.sleep(3)
            clear_terminal()
        else:
            time.sleep(3)
            clear_terminal()
            menu(account_id)
    else:
        print(f"R {transaction_amount} is an invalid transaction amount.")
        time.sleep(5)
        make_deposit(account_id)

def make_withdrawal(account_id):
    transaction_type = 'cash withdrawal'
    transaction_amount = input("Enter the withdrawal amount here: ")
    if transaction_amount.isdigit():
        transaction_amount = int(transaction_amount)
        time_of_transaction = str(datetime.now())
        current_balance = make_database.select_account_balance(account_id)
        if transaction_amount <= current_balance:
            make_database.insert_into_transactions(account_id,transaction_type,transaction_amount,time_of_transaction)
            make_database.update_accounts_balance_withdrawal(transaction_amount,account_id)
            new_balance = make_database.select_account_balance(account_id)
            print(f"\nYou have successfully made a R {transaction_amount} cash withdrawal.\nYour account balance is now {new_balance}")
            continue_or_not = input("Enter E to exit or any other button to return to the main menu: ")
            if continue_or_not == 'E' or continue_or_not == 'e':
                time.sleep(3)
                clear_terminal()
                print("\nExiting program...")
                time.sleep(5)
                clear_terminal()
            else:
                time.sleep(3)
                clear_terminal()
                menu(account_id)
        else:
            difference = transaction_amount - current_balance
            print(f"You have insufficient funds in your account, top up your account with {difference} to make a withdrawal of {transaction_amount}")
            continue_or_not = input("Enter E to exit or any other button to return to the main menu: ")
            if continue_or_not == 'E' or continue_or_not == 'e':
                time.sleep(3)
                clear_terminal()
                print("\nExiting program...")
                time.sleep(5)
                clear_terminal()
            else:
                time.sleep(3)
                clear_terminal()
                menu(account_id)
    else:
        print(f"R {transaction_amount} is an invalid transaction amount.")
        time.sleep(5)
        make_deposit(account_id)

def change_password(userID):
    new_password = getpass.getpass("Enter your new profile password here: ")
    old_password = make_database.select_client_password(userID)
    account_id = make_database.select_account_id(userID)
    if new_password != old_password:
        make_database.update_clients_password(new_password,userID)
        print("\nYou have succesfully changed your profile password")
        continue_or_not = input("Enter E to exit or any other button to return to the main menu: ")
        if continue_or_not == 'E' or continue_or_not == 'e':
            time.sleep(3)
            clear_terminal()
            print("\nExiting program...")
            time.sleep(5)
            clear_terminal()
        else:
            time.sleep(3)
            clear_terminal()
            menu(account_id)
    else:
        print("New password must be different from the old password")
        continue_or_not = input("Enter E to exit or any other button to return to the main menu: ")
        if continue_or_not == 'E' or continue_or_not == 'e':
            time.sleep(3)
            clear_terminal()
            print("\nExiting program...")
            time.sleep(5)
            clear_terminal()
        else:
            time.sleep(3)
            clear_terminal()
            menu(account_id)


def menu(account_id):
    print("\n")
    print("1. Make a cash deposit")
    print("2. Make a cash withdrawal")
    print("3. Check account balance")
    print("4. Change account pin")
    print("5. change profile password")
    print("6. Delete profile")
    # print("7. Delete account")
    # print("8. Delete transaction history")
    print("0. Exit the program")
    print("\n")
    choice = input("Enter the number corresponding with the action you would like to take here: ")
    if choice.isdigit():
        if int(choice) >=1 and int(choice) <=8:
            menu_actions(choice,account_id)
        elif int(choice) == 0:
            time.sleep(5)
            clear_terminal()
            print("\nExiting program...")
            time.sleep(5)
            clear_terminal()
        else:
            print(f"\n\n{choice} is an invalid input")
            time.sleep(5)
            clear_terminal()
            menu(account_id)
    else:
        print(f"\n\n{choice} is an invalid input")
        time.sleep(5)
        clear_terminal()
        menu(account_id)


def menu_actions(choice,account_id):
    if int(choice) == 1:
        time.sleep(3)
        clear_terminal()
        make_deposit(account_id)
    elif int(choice) == 2:
        time.sleep(3)
        clear_terminal()
        make_withdrawal(account_id)
    elif int(choice) == 3:
        time.sleep(3)
        clear_terminal()
        check_balance(account_id)
    elif int(choice) == 4:
        time.sleep(3)
        clear_terminal()
        change_account_pin(account_id)
    elif int(choice) == 5:
        time.sleep(3)
        clear_terminal()
        user_id = make_database.select_client_id(account_id)
        change_password(user_id)
    elif int(choice) == 6:
        time.sleep(3)
        clear_terminal()
        user_id = make_database.select_client_id(account_id)
        delete_profile(user_id,account_id)
    # elif int(choice) == 7:
    #     time.sleep(3)
    #     clear_terminal()
    #     pass
    # elif int(choice) == 8:
    #     time.sleep(3)
    #     clear_terminal()
    #     pass

def menu_backend_logic_layout():
    make_database.build_db()
    user_choice = landing_screen()
    if user_choice == '1':
        details = sign_up()
        username = details[0]
        password = details[1]
        name = details[2]
        surname = details[3]
        email = details[4]
        account_id = details[5]
        account_pin = details[6]
        account_type = 'personal account'
        account_balance = 0
        continue_or_not = input("Enter E to exit or any other button to continue: ")
        if continue_or_not == 'E' or continue_or_not == 'e':
            make_database.insert_into_clients(username,password,name,surname,email)
            make_database.insert_into_accounts(account_id,account_pin,username,account_type,account_balance)
            print(f"\n\nWelcome {username}. We are pleased to be your trusted bank, may we have a fruitful journey.\nCheck your emails for your login details.")
            time.sleep(5)
            clear_terminal()
            print("\nExiting program...")
            time.sleep(5)
            clear_terminal()
        else:
            make_database.insert_into_clients(username,password,name,surname,email)
            make_database.insert_into_accounts(account_id,account_pin,username,account_type,account_balance)
            print(f"\n\nWelcome {username}. We are pleased to be your trusted bank, may we have a fruitful journey.\nCheck your emails for your login details.")
            time.sleep(5)
            clear_terminal()
            menu(account_id)

    elif user_choice == '2':
        account_id = sign_in()
        time.sleep(5)
        clear_terminal()
        if account_id:
            menu(account_id)

menu_backend_logic_layout()

