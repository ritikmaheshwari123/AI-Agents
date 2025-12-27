import array
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)
print("Array elements:")
for element in arr:
    print(element)

import math
print("Square root of 16 is:", math.sqrt(16))
print("Value of pi is:", math.pi)

import random
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

import os
print("Current working directory:", os.getcwd())
os.mkdir('test_directory')

import shutil
shutil.copyfile('source.txt', 'destination.txt')

import json
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print("JSON string:", json_string)
print(type(json_string))

parsed_data = json.loads(json_string)
print("Parsed data:", parsed_data)
print(type(parsed_data))

import csv
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])

with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

from datetime import datetime, timedelta
now = datetime.now()
print("Current date and time:", now)
future_date = now + timedelta(days=10)
print("Date after 10 days:", future_date)

import time
print(time.time())
time.sleep(2)
print(time.time())

import re

pattern = r'\d+'
text = 'There are 3 apples and 5 bananas.'
match = re.search(pattern, text)
print(match.group())

