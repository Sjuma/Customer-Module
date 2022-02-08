import os
import csv


class Product:
    products = []

    def __init__(self, product_id: str, product_name: str, product_quantity: int, product_price: float):
        self.product_id = product_id
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price

        Product.products.append(self)

    # return a string representation of the product instances
    def __repr__(self):
        return f"Product('{self.product_name}', {self.product_id}, {self.product_price})"

    # add a new product to the system


def add_product(quantity=None):
    print('Add a product')
    print()
    _id = input('Enter product id: ')
    with open('products.csv', 'r') as products_file:
        products = csv.reader(products_file)
        products_list = list(products)
        products_ids_list = [item[0] for item in products_list]
        print('Product IDs ', products_ids_list)
        for i in range(len(products_ids_list)):
            if _id == products_ids_list[i]:
                print('Product is in the system')
                print()
                return add_product()

    name = input('Enter product name: ')
    quantity = input('Enter quantity: ')
    price = float(input('Enter product price: '))
    # create a product object from the inputs
    Product(_id, name, quantity, price)

    # write product data into a csv
    with open('products.csv', 'a', newline='') as products_file:
        headers = ['ID', 'Name', 'Quantity', 'Price']
        file_is_empty = os.stat('products.csv').st_size == 0
        writer = csv.writer(products_file)
        if file_is_empty:
            writer.writerow(headers)
        for product in Product.products:
            writer.writerow(
                [product.product_id, product.product_name, product.product_quantity, product.product_price])
            print(product)


# Update products file
def update_products_file(updated_products_list):
    with open('products.csv', 'w', newline='') as products_file:
        products = csv.writer(products_file)
        products.writerows(updated_products_list)


# process user input and update product records

def update_product_records():
    # validate the existence of a product using input ID
    product_id_to_update = input('Enter the ID of the product to be updated: ')
    product_ids_list = []
    with open('products.csv', 'r') as products_file:
        products = csv.reader(products_file)
        for product in products:
            product_ids_list.append(product[0])
        print(product_ids_list)
    product_id = product_ids_list.count(product_id_to_update)
    if product_id == 0:
        print('Invalid ID')
        update_product_records()

    # Proceed to update products file
    else:
        product_to_update = []
        updated_products_list = []
        with open('products.csv', 'r') as products_file:
            products = csv.reader(products_file)
            for product in products:
                if product[0] == product_id_to_update:
                    product_to_update.append(product)
                elif product[0] != product_id_to_update:
                    updated_products_list.append(product)
        update_products_file(updated_products_list)

        # update product's records/details
        print(product_to_update)
        name = input('Enter new product name: ')
        product_to_update[0][1] = name
        quantity = input('Enter product quantity: ')
        product_to_update[0][2] = quantity
        price = input('Enter new price: ')
        product_to_update[0][3] = price
        print(product_to_update)

        # write new product details in products csv file
        with open('products.csv', 'a', newline='') as products_file:
            writer = csv.writer(products_file)
            for product in product_to_update:
                writer.writerow([product_id_to_update, name, quantity, price])


# view all product details

def view_products():
    with open('products.csv', 'r') as products_file:
        products = csv.reader(products_file)
        for product in products:
            print(product)


# delete a product from products csv file

def remove_product():
    with open('products.csv', 'r+') as products_file:
        products = products_file.readlines()
        products_file.seek(0)

        input_id = input('Enter the ID of the product to be deleted ')
        for product in products:
            if input_id not in product.split(',')[0]:
                products_file.write(product)
            products_file.truncate()
        print(f'product has been deleted: ')

# add_product()
# view_products()
# update_product_records()
# remove_product()
