# bounce.py
#
# Exercise 1.5

height = 100 # meters
num_of_bounces = 1

while num_of_bounces <= 10:
    num_of_bounces = num_of_bounces + 1
    height = ( height / 5 ) * 3
    print(round(height, 4))
