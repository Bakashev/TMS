import json
import random

number_line = int(input('Enter number of line: '))
number_column = int(input('Enter number of column: '))
list_number_random = [[random.randint(20, 40) for _ in range(number_line)] for _ in range(number_column)]
dict_list = {index: value for index, value in enumerate(list_number_random)}
for row in list_number_random:
    print(row)



