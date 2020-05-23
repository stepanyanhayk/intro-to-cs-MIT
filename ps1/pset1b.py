"""
Created on May 21, 2020

@author: Hayk Stepanyan
Problem set 1: Saving, with a rise
"""

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_rise = float(input("Enter the semi-annual rise, as a decimal: "))
r = 0.04
portion_down_payment = 0.25
current_saving = 0
month_count = 0

while current_saving < total_cost * portion_down_payment:
    month_count += 1
    current_saving = current_saving + annual_salary / 12 * portion_saved + current_saving * r / 12
    if month_count % 6 == 0:
        annual_salary = annual_salary + annual_salary * semi_annual_rise
print("Number of months:", month_count)
