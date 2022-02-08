from customer import *
from product import *
from purchase import *
import csv


def main_menu():
    print('starting')

    main_menu_operation = 0
    while main_menu_operation != '0':
        main_menu_operation = input(''''
                                        WELCOME: MAIN MENU
                                                                                                                        
                                        1.Customer operations 
                                        2.Product operations 
                                        3.Purchase operations
                                        0.Exit
                                        
                                        Select operation to perform:
                                        
                                        ''')

        while main_menu_operation == '1':
            print()
            customer_operations = input('''
            
                                        CUSTOMER OPERATIONS
                                        
                                        1.Add customer
                                        2.View all customers  
                                        3.Update customer records
                                        4.Delete a customer
                                        0.Exit 
                                        
                                        Select customer operation:   
                                              
                                        ''')

            if customer_operations == '1':
                add_customer()
            elif customer_operations == '2':
                view_customers()
            elif customer_operations == '3':
                update_customer_records()
            elif customer_operations == '4':
                remove_customer()
            elif customer_operations == '0':
                print('Back to main menu')
                break
            else:
                print('Invalid input')

        while main_menu_operation == '2':
            print()
            product_operations = input('''
            
                                        Product operations
                                        
                                        1.Add product
                                        2.View all products  
                                        3.Update product records
                                        4.Delete a product
                                        0.Exit   
                                        
                                        Select product operation
                                        ''')

            if product_operations == '1':
                add_product()
            elif product_operations == '2':
                view_products()
            elif product_operations == '3':
                update_product_records()
            elif product_operations == '4':
                remove_product()
            elif product_operations == '0':
                print('Back to main menu')
                break
            else:
                print('Invalid input')

        while main_menu_operation == '3':
            print()
            purchase_operations = input('''
                                        Purchase operations 
                                        
                                        1. Purchase products.
                                        0. Exit
                                        ''')
            if purchase_operations == '1':
                pass
                find_customer()
                product_purchase()
            elif purchase_operations == '0':
                print('Back to main menu')
                break
            else:
                print('Invalid input')


main_menu()
