import os
import random
import make_database
import time

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

def sign_up():
    id = input("Enter your username here: ")
    if id:
        password = input("Enter your password here: ")
        if password:
            first_name = input("Enter your first name here: ")
            if first_name:
                surname = input("Enter your surname here: ")
                if surname:
                    email = input("Enter your email here: ")
                    if email:
                        print(f"Welcome {id}. We are pleased to be your trusted bank, may we have a fruitful journey.")
                        time.sleep(3)
                        clear_terminal()
                    else:
                        print("An email is required.\n")
                        time.sleep(5)
                        sign_up()
                else:
                    print("A surname is required.\n")
                    time.sleep(5)
                    sign_up()
            else:
                print("A password is required.\n")
                time.sleep(5)
                sign_up()
        else:
            print("A password is required.\n")
            time.sleep(5)
            sign_up()
    else:
        print("A username is required.\n")
        time.sleep(5)
        sign_up()

    return id,password,first_name,surname,email

def sign_in():
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



