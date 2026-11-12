# self-assessment
# 1. compared to doing this in excel, i'd imagine that this is significantly faster and simpler due to less bloatware. python can handle a lot more data and has more tools (ex. matplotlib) available, and can also be controlled better from git. but, excel is easier for non-coders, is widely supported in businesses, and might be quicker for better visual data manipulation.
# 2. a real business process that'd benefit from an append-mode log file would be 

# exercise 1: get the file - done
# exercise 2: read and print raw rows
with open(sales.csv):
    for row in csv.reader(sales.csv):
        print(['product', 'price', 'quantity'])
print()

# exercise 3: skip the header
print()

# exercise 4: compute totals
print()

# exercise 5: filter and write
print()

# exercise 6: csv.DictReader
print()

# exercise 7: Sales summary by product
print()

# exercise 8: Append mode log
print()
