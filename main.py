from customer import Customer
from product import Product
from purchase import Purchase


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    juma = Customer()
    juma.add_customer()

    ''''''
    fresha = Product()
    fresha.add_product()

    purchase = Purchase()
    purchase.add_purchase()
