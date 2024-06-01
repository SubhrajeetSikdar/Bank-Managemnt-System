Description
This is a simple command-line Bank Account Management System implemented in Python. It allows users to create accounts, deposit and withdraw funds, check balances, manage account types, and apply for loans. The system is integrated with MySQL for data storage.

Features:
-> Create bank accounts with initial balances and account types.
-> Deposit funds into existing accounts.
-> Withdraw funds from existing accounts with sufficient balance.
-> Check balances of existing accounts.
-> Manage account types (debit, credit, or both).
-> Apply for loans based on annual income.


Database Schema:
The system uses a MySQL database named bank with a single table named accounts. The table schema is as follows:
       CREATE TABLE accounts (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       balance FLOAT NOT NULL,
       account_type ENUM('debit', 'credit', 'both') NOT NULL
       );


Instructions:
-> Set up a MySQL server and create a database named bank.
-> Create a table named accounts in the bank database using the provided schema.
-> Configure the MySQL connection settings in the Python code (main.py) (host, user, password).
-> Run the Python code using a compatible Python interpreter.
->Follow the on-screen instructions to interact with the Bank Account Management System.

Requirements
-> Python 3.x
-> MySQL Server
-> mysql-connector-python library (install using pip install mysql-connector-python)


How to Run:
-> Clone this repository to your local machine.
-> Set up a MySQL server and create a database named bank.
-> Create a table named accounts in the bank database using the provided schema.
-> Update the MySQL connection settings in the Python code (main.py) if necessary.
-> Run the Python code using a compatible Python interpreter.
