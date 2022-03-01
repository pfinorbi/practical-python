# pcost.py
#
# Exercise 1.27
import csv
from fileinput import filename
import sys

def portfolio_cost(filename):   
    count = 0
    total_cost = 0.0

    with open(filename, 'rt') as portfolio:
        rows = csv.reader(portfolio)
        for row in rows:
            if(count > 0):

                try:
                    current_share = int(row[1])
                except ValueError:
                    print(f"Couldn't cast value to integer. Affected row: {row}")
                try:
                    current_price = float(row[2])
                except ValueError:
                    print(f"Couldn't cast value to float. Affected row: {row}")
                
                total_cost = total_cost + (current_share * current_price)
            
            count = count + 1
        
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')