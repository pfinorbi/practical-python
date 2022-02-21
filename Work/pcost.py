# pcost.py
#
# Exercise 1.27
count = 0
total_cost = 0.0

with open('Data/portfolio.csv', 'rt') as portfolio:
    for row in portfolio:
        if(count > 0):
           shares_and_prices = row.split(',')
           current_share = int(shares_and_prices[1])
           current_price = float(shares_and_prices[2])
           total_cost = total_cost + (current_share * current_price)
        count = count + 1

print(f'Total cost: {total_cost}')