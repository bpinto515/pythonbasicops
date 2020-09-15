#!/usr/bin/env python3
#
# BASIC SCRIPT FOR CSV FILES MANIPULATION 

import os
import csv

# to print the list
def print_list(list_data, list_type):
    print("\nHere is the listing of {}:".format(list_type))
    for item in list_data:
        print(item)

# set up the working directory, file_name, full file path
file_name = 'customers.csv'
new_file_name = 'new_customers.csv'
my_file = os.path.join('/home/bmp/Documents/PythonThings', file_name)
my_new_file = os.path.join('/home/bmp/Documents/PythonThings', new_file_name)

# read from a csv file
customer_file = open(my_file)
customer_reader = csv.reader(customer_file)
customer_data = list(customer_reader)
print("\npassing the reader to list() creates a list of lists:")
print(customer_data)
input("\npress Enter to continue...\n")
print_list(customer_data, 'customers')
input("\npress Enter to continue...\n")
print(customer_data[1][1] + ' email: ' + customer_data[1][2])
input("\npress Enter to continue...\n")
customer_file.close()

#write on csv file
customer_file = open(my_new_file, 'w', newline='')
customer_writer = csv.writer(customer_file)
for i in customer_data:
    customer_writer.writerow(i)
print("\nSuccessfully created new customer data file...")
input("\npress Enter to continue...\n")