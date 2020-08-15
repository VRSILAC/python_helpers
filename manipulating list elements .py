"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A

# first get the indices of all the calling numbers in the calls data which has the area code (080)

def return_bangalore_number_indices(my_list, subs):
    indices = []
    for sublist in my_list:
        if subs in sublist[0]:
            indices.append(my_list.index(sublist))
    return indices

# subset the calls data based on the list of indexes from the above function

bangalore_numbers = [calls[i] for i in return_bangalore_number_indices(calls, subs)]

# retrieve the unique set of receiving numbers from (080) area code

receiving_numbers = [i[1] for i in bangalore_numbers]
print(set(receiving_numbers)

# getting all the unique fixed line area codes
      
start = '('
end = ')'
fixed_line_codes = set([i[i.find(start):i.rfind(end)+1] for i in list(unique_receiving_numbers) if '(' in i])
      
# getting all mobile receiving numbers
      
unique_mobile_numbers_7 = [element for element in unique_receiving_numbers if element.startswith('7') ]
unique_mobile_numbers_8 = [element for element in unique_receiving_numbers if element.startswith('8') ]
unique_mobile_numbers_9 = [element for element in unique_receiving_numbers if element.startswith('9') ]
all_mobile_numbers = set(unique_mobile_numbers_7 + unique_mobile_numbers_8 + unique_mobile_numbers_9)

#  extracting area codes for the mobile numbers
      
mobile_start = 0
mobile_end = ' '
mobile_area_codes = set([i[0:i.rfind(mobile_end)+1] for i in list(all_mobile_numbers)])
mobile_area_codes  
      
# getting all unique telemarketers
      
unique_telemarketers = set([element for element in unique_receiving_numbers if element.startswith('140') ])
unique_telemarketers
      
# joining all three sets
      
all_receiving_codes = fixed_line_numbers.union(mobile_area_codes).union(unique_telemarketers)
      
# printing all the area codes together
      
print('The numbers called by people in Bangalore have codes:', all_receiving_codes)
      
# Part B
      
print(str(round(len(fixed_line_codes)/len(all_receiving_codes), 2)), 'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')