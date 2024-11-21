import sqlite3
from flask import Flask, request, jsonify

dtbase = "bank.db"
def create_db_file():
    connection = sqlite3.connect(dtbase)
    return connection

def build_db():

    with create_db_file() as connect:
        database = connect.cursor()

        #create a table for accountholders, name it clients
        database.execute("CREATE TABLE IF NOT EXISTS Clients(user_id TEXT PRIMARY KEY, user_password TEXT NOT NULL,user_first_name TEXT NOT NULL,user_surname TEXT NOT NULL,user_email TEXT NOT NULL)")

        #create a table for accounts, name it accounts
        database.execute("CREATE TABLE IF NOT EXISTS Accounts(account_id TEXT PRIMARY KEY, account_pin TEXT NOT NULL, user_id TEXT NOT NULL, account_type TEXT, account_balance INTEGER)")

        #create a table for transactions, name it transactions
        database.execute("CREATE TABLE IF NOT EXISTS Transactions(transaction_id TEXT PRIMARY KEY AUTOINCREMENT, account_id TEXT NOT NULL, transaction_type TEXT, transaction_amount INTEGER)")

        #saving changes
        connect.commit()

def insert_into_clients(*user_details):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("INSERT INTO Clients(user_id,user_password,user_first_name,user_surname,user_email) VALUES (?,?,?,?,?)",user_details)
        connect.commit()

def insert_into_accounts(*account_details):
    with create_db_file() as connect:
        conn  = connect.cursor()
        conn.execute("INSERT INTO Accounts(account_id,account_pin,user_id,account_type,account_balance) VALUES (?,?,?,?,?)",account_details)
        connect.commit()

def insert_into_transactions(*transaction_details):
    with create_db_file() as connect:
        conn = connect.cursor()
        conn.execute("INSERT INTO Transactions(account_id,transaction_type,transaction_amonut) VALUES (?,?,?)",transaction_details)
        connect.commit()




