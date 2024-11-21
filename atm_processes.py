import os
import random
import time
from make_database import insert_into_clients,insert_into_accounts,insert_into_transactions

digits = [0,1,2,3,4,5,6,7,8,9]

def clear_terminal():
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

def change_account_pin():
    new_pin = input("Enter your new 5 digit pin here: ")
    if not new_pin.isdigit():
        print("Pin must be made of digits only")
        time.sleep(5)
        clear_terminal()
    elif len(new_pin)<5:
        print("Pin must be 5 digits long")
        time.sleep(5)
        clear_terminal()
    else:
        #print("You have successfully updated your pin")
        return new_pin

def sign_up():
    credential_list = []
    id = input("Enter your username here: ")
    if id:
        credential_list.append(id)
        password = input("Enter your password here: ")
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
                        print(f"\nWelcome {id}. We are pleased to be your trusted bank, may we have a fruitful journey.\n")
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

    return tuple(credential_list)

def sign_in():
    user_id = input("Enter your username here: ")
    user_password = input("Enter your password here: ")
    pass

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

def menu_display():
    if landing_screen() == '1':
        details = sign_up()
        continue_or_not = input("Enter E to exit or any other button to continue: ")
        if continue_or_not == 'E' or continue_or_not == 'e':
            time.sleep(3)
            clear_terminal()
        else:
            insert_into_clients(details)
            print("You have successfully created an account with us, we're happy to have you.")
    elif landing_screen() == '2':
        sign_in()

