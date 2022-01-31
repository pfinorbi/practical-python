# mortgage.py
#
# Exercise 1.7

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

    print(str(count_of_months) + " " + str(round(total_paid, 2)) + " " + str(round(principal, 2)))

    count_of_months = count_of_months + 1

print('Total paid:', round(total_paid, 2))
print('Total number of months:', count_of_months - 1)
