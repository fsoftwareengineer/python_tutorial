import uuid
customers = []


class Customer:
    id = ""
    name = ""


def insert_customer(customer_name):
    c = Customer()
    c.id = uuid.uuid4()
    c.name = customer_name
    customers.append(c)


def print_customer():
    for customer in customers:
        print("[" + str(customer.id) + "] " + customer.name)
