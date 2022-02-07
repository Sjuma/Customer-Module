from customer import *
from product import *
import csv
import os


def main_menu():
    while True:
        print('''
        Welcome come to retail CRM system
        
        CUSTOMER OPERATIONS
        
        1.Add a customer
        2.View customers 
        3.Update a customer record
        4. Delete a customer
        0. exist
        ''')

        operation = input('Enter select operations to perform: ')

        if operation == '1':
            print('Add a new customer')
            Customer.add_customer()
        elif operation == '2':
            print('View Customers')
            Customer.view_customers()
        elif operation == '3':
            print("Update a Customer's")
            Customer.update_customer_records()
        elif operation == '4':
            print("Delete a Customer's")
            Customer.remove_customer()
        elif operation == '0':
            print('Exit the program')
            break
        else:
            print('Enter a valid choice to run an operation ')


# main_menu()
