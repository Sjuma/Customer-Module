import csv
import os
import tarfile


class Customer:
    customers = []

    def __init__(self, customer_name, customer_id, customer_address):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.customer_address = customer_address

        Customer.customers.append(self)

    # return a string representation of every object
    def __repr__(self):
        return f"Customer('{self.customer_name}',{self.customer_id},{self.customer_address})"

    # add a new customer to the system


def add_customer():
    # validate that the input ID is unique
    global _id
    _id = input("Please enter the customer ID you want to add: ")
    with open('customers.csv', 'r') as customers_file:
        customers = csv.reader(customers_file)
        customers_list = list(customers)
        customers_ids_list = [item[0] for item in customers_list]
        # print(customers_ids_list)
        for i in range(len(customers_ids_list)):
            if _id == customers_ids_list[i]:
                print(customers_ids_list[i])
                print('Customer is in the system')
                return add_customer()
    name = input("Enter new customer's name: ")
    address = input("Please enter the customer's address: ")
    # create new product object
    Customer(_id, name, address)

    # add customer to customers csv file
    with open('customers.csv', 'a', newline='') as customer_file:
        headers = ['ID', 'Name', 'Address']
        file_is_empty = os.stat('customers.csv').st_size == 0
        writer = csv.writer(customer_file)
        if file_is_empty:
            writer.writerow(headers)
        for customer in Customer.customers:
            writer.writerow([customer.customer_name, customer.customer_id, customer.customer_address])
            print(Customer.customers)

    # list all th customers in the system

def view_customers():
    with open('customers.csv', 'r') as customers_file:
        customers = csv.reader(customers_file)
        for customer in customers:
            print(customer)

    # Update customers file

def update_customer_file(updated_customers_list):
    with open('customers.csv', 'w', newline='') as customers_file:
        writer = csv.writer(customers_file)
        writer.writerows(updated_customers_list)

    # process user input and update customer records

def update_customer_records():
    customer_id_to_update = input('Enter the ID of the customer to update: ')
    customer_ids_list = []
    with open('customers.csv', 'r') as customers_file:
        customers = csv.reader(customers_file)
        for customer in customers:
            customer_ids_list.append(customer[0])
    print(customer_ids_list)
    customer_id = customer_ids_list.count(customer_id_to_update)
    if customer_id == 0:
        print('Invalid ID')
        print()
        update_customer_records()

    # Proceed to update customers file
    else:
        customer_to_update = []
        updated_customers_list = []
        with open('customers.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == customer_id_to_update:
                    customer_to_update.append(row)
                elif row[0] != customer_id_to_update:
                    updated_customers_list.append(row)
        update_customer_file(updated_customers_list)

        # update customer's records/details
        print(customer_to_update)
        name = input("Update customer's name: ")
        customer_to_update[0][1] = name
        address = input("Enter customer's address: ")
        customer_to_update[0][2] = address
        print(customer_to_update)

        # insert new customer details to the customer's csv
        with open('customers.csv', 'a', newline='') as customers_file:
            writer = csv.writer(customers_file)
            for customer in customer_to_update:
                writer.writerow([customer_id_to_update, name, address])

    # delete customer details after receiving user id

def remove_customer():
    with open('customers.csv', 'r+') as customers_file:
        lines = customers_file.readlines()
        customers_file.seek(0)

        input_id = input('Enter the ID of the customer to be deleted: ')
        for line in lines:
            if input_id not in line.split(',')[0]:
                customers_file.write(line)
            customers_file.truncate()
        print('customer has been deleted')

    '''
    @classmethod
    def check_customer(cls):
        input_id = input("Enter customer's id: ")
        with open('customers.csv', 'r') as customers_file:
            customers = csv.reader(customers_file)
            customers_list = list(customers)
            customers_ids_list = [item[1] for item in customers_list]
            print(customers_ids_list)
            for i in range(len(customers_list)):
                if input_id in customers_ids_list:
                    print()
                    return print('customer found')
                else:
                    print('Invalid id. Enter new id')
                    return cls.check_customer()
    '''


# add_customer()
# view_customers()
# remove_customer()
# update_customer_records()
