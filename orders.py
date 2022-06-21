import csv
import sys
from collections import Counter

file_name = sys.argv[1]

brands_popularity = dict()
product_dictionary = dict()

with open(f'./{file_name}') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    number_of_orders = 0

    for order in csv_reader:
        product = order[2]
        number_of_orders += 1
        
        if product not in product_dictionary:
            product_dictionary[product] = 0

        product_dictionary[product] += int(order[3])

        if product not in brands_popularity:
            brands_popularity[product] = []

        brands_popularity[product].append(order[4])

# First file
with open(f'./0_{file_name}', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for key, value in product_dictionary.items():
        writer.writerow([key, value / number_of_orders])
        
# Second file
with open(f'./1_{file_name}', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for key in product_dictionary:
        writer.writerow([key, Counter(brands_popularity[key]).most_common()[0][0]])
   