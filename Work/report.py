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
      holding = dict(zip(headers, row))
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

def make_report(portfolio, prices):

  stock_changes = []

  for item in portfolio:
    stock_changes.append((item['name'], int(item['shares']), float(prices[item['name']]), float(prices[item['name']]) - float(item['price'])))
  
  return stock_changes

portfolio = read_portfolio('Data/portfoliodate.csv')

prices = read_prices('Data/prices.csv')

purchase_value = 0.0
current_value = 0.0

for element in portfolio:
  #print(f"{ element['name'] }: { element['shares'] * prices[element['name']] }")
  purchase_value += int(element['shares']) * float(element['price'])
  current_value += int(element['shares']) * float(prices[element['name']])
  
profit = current_value - purchase_value

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
formatted_headers = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'

separator = []

for h in headers:
  separator.append(f'{h.replace(h,"-"):->10s}')

print("\nSummary:\n")
print(f"Purchase value: {purchase_value}")
print(f"Current value: {current_value}")
print(f"Profit: {profit:.2f}")

print("\nDetailed price change report:\n")
print(formatted_headers)
print(f'{separator[0]} {separator[1]} {separator[2]} {separator[3]}')

for name, shares, price, change in report:
  updated_price = str(price).replace(str(price), "$"+str(price))
  print(f'{name:>10s} {shares:>10d} {updated_price:>10s} {change:>10.2f}')

print("\n")