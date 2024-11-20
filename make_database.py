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
        database.execute("CREATE TABLE IF NOT EXISTS Clients(user_id TEXT PRIMARY KEY,user_first_name TEXT,user_surname TEXT,user_email TEXT)")

        #create a table for accounts, name it accounts
        database.execute("CREATE TABLE IF NOT EXISTS Accounts(account_id TEXT PRIMARY KEY, user_id TEXT NOT NULL, account_type TEXT, account_balance INTEGER, account_status TEXT)")

        #create a table for transactions, name it transactions
        database.execute("CREATE TABLE IF NOT EXISTS Transactions(transaction_id TEXT PRIMARY KEY, account_id TEXT NOT NULL, transaction_type TEXT, transaction_amount INTEGER)")

        #saving changes
        connect.commit()


