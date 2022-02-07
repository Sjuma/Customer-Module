import csv
from customer import *

purchasing_customer = []
purchased_products = []
product_purchases = []


# check if the customer exists in the system
def find_customer():
    # global _id
    _id = input('Enter the customer ID: ')
    purchasing_customer_id = []
    with open('customers.csv', 'r') as customers_file:
        customers = csv.reader(customers_file)
        for customer in customers:
            purchasing_customer_id.append(customer[0])
        purchase_id = purchasing_customer_id.count(_id)

        # print(purchase_id)
        # print(customer)
        if purchase_id == 0:
            print('Customer not found')
            find_customer()
        # get customer details
        else:
            with open('customers.csv', 'r') as file:
                customers = csv.reader(file)
                for row in customers:
                    if row[0] == _id:
                        purchasing_customer.append(row)
                print('The customer is: ' + purchasing_customer[0][1])


def product_purchase():
    product_to_purchase_id = []
    input_product_id = input('Enter product ID: ')
    with open('products.csv', 'r') as products_file:
        products = csv.reader(products_file)
        for product in products:
            product_to_purchase_id.append(product[0])
        product_id = product_to_purchase_id.count(input_product_id)

        if product_id == 0:
            print('Product does not exist')
            product_purchase()

    with open('products.csv', 'r') as file:
        products = csv.reader(file)
        for product in products:
            if product[0] == input_product_id:
                purchased_products.insert(0, product)
        prod_name = purchased_products[0][1]
        prod_quantity = int(purchased_products[0][2])
        prod_price = float(purchased_products[0][3])

        print('product: ' + prod_name)
        print('Quantity in stock: ' + str(prod_quantity))
        print('Unit price: ' + str(prod_price))

    purchase_quantity = int(input('Enter the purchase quantity: '))

    # compare available stock to purchase quantity
    print('checking product quantity')
    if purchase_quantity > prod_quantity:
        print('In stock ' + str(prod_quantity))
        product_purchase()
    else:
        purchase_cost = purchase_quantity * prod_price

        product_purchases.append([input_product_id, prod_name, prod_price, purchase_quantity, purchase_cost])
        print(product_purchases)

        subsequent_purchase = input('''
                                    Enter choice
                                    1. Purchase other items
                                    2. Complete purchase order                                        
                                    ''')

        if subsequent_purchase == '1':
            product_purchase()
        elif subsequent_purchase == '2':
            complete_purchase()


# product_purchase()


def complete_purchase():
    total_cost = 0
    for purchase in product_purchases:
        total_cost += purchase[4]
    print('Total purchase cost: ' + str(total_cost))

    payment_amount = int(input("Enter the customer's payment: "))

    if payment_amount < total_cost:
        print('Your payment amount is less than purchase cost')
        option = input('''
                                    Enter your choice
                                    1. Give a different amount
                                    2. Terminate sell 
                                ''')
        print('resubmitting payment')
        if option == '1':
            complete_purchase()
        elif option == '2':
            print('Transaction terminated')

    else:
        customers_balance = payment_amount - total_cost
        print('Balance is: ' + str(customers_balance))

        update_stock()


def update_stock():
    for purchase in product_purchases:
        product_id = purchase[0]
        quantity = int(purchase[3])

        purchased_prods = []
        updated_stock = []

        with open('products.csv', 'r') as prod_file:
            products = csv.reader(prod_file)
            for product in products:
                if product[0] == product_id:
                    purchased_prods.append(product)
                elif product[0] != product_id:
                    updated_stock.append(product)
        # print(purchased_prods)
        with open('products.csv', 'w', newline='') as stock_file:
            stock = csv.writer(stock_file)
            stock.writerows(updated_stock)

        product_name = purchased_prods[0][1]
        # checking prod quantity 1
        prod_quantity = int(purchased_prods[0][2])
        print(prod_quantity)  # checking prod quantity 2
        print('purchased quantity' + str(quantity))
        purchased_prods[0][2] = prod_quantity - quantity
        print(purchased_prods)  # checking prod quantity 3
        new_stock_quantity = purchased_prods[0][2]
        price = purchased_prods[0][3]
        with open('products.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            for prod in purchased_prods:
                writer.writerow([product_id, product_name, new_stock_quantity, price])
        print('completed updating stock')


find_customer()
product_purchase()
