#!/usr/bin/env python3
#
## BASIC SCRIPT FOR XML FILE OPERATIONS

import os
import xml.etree.ElementTree as et

# set up the working directory, file_name, full file path
working_dir = 'PythonThings'
file_name = 'customers.xml'
my_file = os.path.join('/home/bmp/Documents/', working_dir, file_name)

# read from an xml file and print to console
tree = et.parse(my_file)
root = tree.getroot()
print("\nthe root tag is:")
print(root.tag)
input("npress Enter to continue...\n")

print("\nlist the tag and attrib for children nodes:")
for child in root:
    print(child.tag, child.attrib)
input("npress Enter to continue...\n")

for customer in root.findall('customer'):
    country = customer.find('country').text
    name = customer.get('name')
    print(name + ': ', country)

input("npress Enter to continue...\n")
for customer in root.findall('customer'):
    customer_email = customer.find('customer_email').text
    name = customer.get('name')
    print(name + ': ', customer_email)
input("npress Enter to continue...\n")