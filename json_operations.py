#!/usr/bin/env python3
#
## BASIC SCRIPT FOR JSON FILE OPERATIONS

import os
import json

# to print the customers
def print_customers(d_data, data_type, data_col):
    print("\nHere is the list of {}:".format(data_type))
    for item in d_data:
        print(item[data_col])

# set up the working directory, file_name, full file path
working_dir = 'PythonThings'
file_name = 'customers.json'
my_file = os.path.join('/home/bmp/Documents/', working_dir, file_name)

# read from a json file and print to console
customer_open = open(my_file)
customer_data = json.load(customer_open)
print(customer_data)
input("\npress Enter to continue...\n")

print_customers(customer_data, 'customers', 'customer_name')
input("\npress Enter to continue...\n")

print_customers(customer_data, 'customers_emails', 'customer_email')
input("\npress Enter to continue...\n")

print_customers(customer_data, 'customers_prov_state', 'prov_state')
input("\npress Enter to continue...\n")
