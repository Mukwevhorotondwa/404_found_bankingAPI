import sqlite3
from flask import Flask, request, jsonify
#from atm_processes import sign_up
dtbase = "bank.db"
def create_db_file():
    connection = sqlite3.connect(dtbase)
    return connection

#Creating
def build_db():

    with create_db_file() as connect:
        database = connect.cursor()

        #create a table for accountholders, name it clients
        database.execute("CREATE TABLE IF NOT EXISTS Clients(user_id TEXT PRIMARY KEY, user_password TEXT NOT NULL,user_first_name TEXT NOT NULL,user_surname TEXT NOT NULL,user_email TEXT NOT NULL)")

        #create a table for accounts, name it accounts
        database.execute("CREATE TABLE IF NOT EXISTS Accounts(account_id TEXT PRIMARY KEY, account_pin TEXT NOT NULL, user_id TEXT NOT NULL, account_type TEXT, account_balance INTEGER)")

        #create a table for transactions, name it transactions
        database.execute("CREATE TABLE IF NOT EXISTS Transactions(transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, account_id TEXT NOT NULL, transaction_type TEXT, transaction_amount INTEGER)")

        #saving changes
        connect.commit()

#Inserting
def insert_into_clients(id,password,first_name,surname,email):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("INSERT INTO Clients(user_id,user_password,user_first_name,user_surname,user_email) VALUES (?,?,?,?,?)",(id,password,first_name,surname,email))
        connect.commit()

def insert_into_accounts(accountID,acoountPIN,userID,accountType,accountBalance):
    with create_db_file() as connect:
        conn  = connect.cursor()
        conn.execute("INSERT INTO Accounts(account_id,account_pin,user_id,account_type,account_balance) VALUES (?,?,?,?,?)",(accountID,acoountPIN,userID,accountType,accountBalance))
        connect.commit()

def insert_into_transactions(accountID,transactionType,transactionAmount):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("INSERT INTO Transactions(account_id,transaction_type,transaction_amount) VALUES (?,?,?)",(accountID,transactionType,transactionAmount))
        connect.commit()

#updating
def update_clients(password,id):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("UPDATE Clients SET user_password=? WHERE user_id=?",(password,id))
        conn.commit()

def update_accounts_pin(pin,id):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("UPDATE Accounts SET account_pin=? WHERE account_id=?",(pin,id))
        connect.commit()

def update_accounts_balance_deposit(balance,id):
    with create_db_file() as connect:
        conn = connect.cursor()
        old_balance = select_account_balance(id)
        balance = old_balance + balance
        conn.execute("UPDATE Accounts SET account_balance=? WHERE account_id=?",(balance,id))
        connect.commit()

def update_accounts_balance_withdrawal(balance,id):
    with create_db_file() as connect:
        conn = connect.cursor()
        old_balance = select_account_balance(id)
        balance = old_balance - balance
        conn.execute("UPDATE Accounts SET account_balance=? WHERE account_id=?",(balance,id))
        connect.commit()

#Deleting
def delete_clients(userID):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("DELETE FROM Clients WHERE user_id=(?)",(userID,))
        #delete_accounts_all(userID)
        connect.commit()

def delete_accounts_specific(accountID):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("DELETE FROM Accounts WHERE account_id=(?)",(accountID,))
        connect.commit()
    
def delete_accounts_all(userID):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("DELETE FROM Accounts WHERE user_id=(?)",(userID,))
        connect.commit()

def delete_transactions_single_account_all(accountID):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("DELETE FROM Transactions WHERE account_id=(?)",(accountID,))
        connect.commit()
#Selecting
def select_account_balance(accountID):
    with create_db_file() as connect:
        conn = connect.cursor()
        account_balance = conn.execute("SELECT account_balance FROM Accounts WHERE Account_id=(?)",(accountID,))
        account_balance_converted = account_balance.fetchall()
        return account_balance_converted[0][0]

#build_db()
#insert_into_clients("Tsipora","1@Thisguy","Tshepo","Majoro","mothofeelama@gmail.com")



