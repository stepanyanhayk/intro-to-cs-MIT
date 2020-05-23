"""
Created on May 22, 2020

@author: Hayk Stepanyan
Problem set 1: Finding the right amount to save away
"""

bisection_step = 0
annual_salary_original = float(input("Enter your starting annual salary: "))
total_cost = 1000000.0
semi_annual_rise = 0.07
r = 0.04
portion_down_payment = 0.25
current_saving = 0
month_count = 36

low_rate = 0
high_rate = 10000
guess = (low_rate + high_rate) / 2.0

while True:
    current_saving = 0
    annual_salary = annual_salary_original
    for month in range(month_count):
        current_saving = current_saving + annual_salary / 12 * guess / 10000 + current_saving * r / 12
        if (month + 1) % 6 == 0:
            annual_salary = annual_salary + annual_salary * semi_annual_rise

    if current_saving < total_cost * portion_down_payment:
        low_rate = guess
    else:
        high_rate = guess

    if low_rate == high_rate:
        print("It is not possible to pay the down payment in three years")
        break

    if abs(current_saving - total_cost * portion_down_payment) <= 100:
        portion_saved = int(guess) / 10000
        print("Best saving rate:", portion_saved)
        print("Steps in bisection search:", bisection_step)
        break

    guess = (high_rate + low_rate) / 2.0
    bisection_step += 1
