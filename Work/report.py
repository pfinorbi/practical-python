# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
  
  portfolio = []

  with open(filename, 'rt') as file:
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
      #holding = (row[0], int(row[1]), float(row[2]))
      holding = {
        headers[0] : row[0],
        headers[1] : int(row[1]),
        headers[2] : float(row[2]) 
      }
      portfolio.append(holding)
  return portfolio

def read_prices(filename):
  
  prices = {}

  with open(filename, 'rt') as file:
    rows = csv.reader(file)
    for row in rows:
      try:
        prices[row[0]] = float(row[1])
      except IndexError:
        pass
  return prices

portfolio = read_portfolio('Data/portfolio.csv')
#print(portfolio)

prices = read_prices('Data/prices.csv')
#print(prices)

purchase_value = 0.0
current_value = 0.0

for element in portfolio:
  #print(f"{ element['name'] }: { element['shares'] * prices[element['name']] }")
  purchase_value += element['shares'] * element['price']
  current_value += element['shares'] * prices[element['name']]
  
profit = current_value - purchase_value

print(f"Purchase value: {purchase_value}")
print(f"Current value: {current_value}")
print(f"Profit: {profit:.2f}")
