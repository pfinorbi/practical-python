# mortgage.py
#
# Exercise 1.7

from posixpath import splitext


principal = 500000.0
rate = 0.05
payment = 2684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

payment_during_extra_period = payment + extra_payment

total_paid = 0.0
count_of_months = 1

while principal > 0:
    if count_of_months >= extra_payment_start_month and count_of_months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - payment_during_extra_period
        total_paid = total_paid + payment_during_extra_period
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

    if principal < 0:
        total_paid = total_paid - abs(principal)
        principal = 0.0

    monthly_status = f'Month {count_of_months} | Total paid: ${total_paid:0.2f} | Remaining amount: ${principal:0.2f}'
    print(monthly_status)

    count_of_months = count_of_months + 1

splitter = f'{60 * "-"}'
total_payment = f'Total paid amount: ${total_paid:0.2f}'
total_months = f'Total number of months needed: {count_of_months - 1}'

print(splitter)
print(total_payment)
print(total_months)
