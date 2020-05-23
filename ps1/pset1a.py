"""
Created on May 20, 2020

@author: Hayk Stepanyan
Problem set 1: House Hunting
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
r = 0.04
portion_down_payment = 0.25
current_saving = 0
month_count = 0

while current_saving < total_cost * portion_down_payment:
    month_count += 1
    current_saving = current_saving + annual_salary / 12 * portion_saved + current_saving * r / 12
print("Number of months:", month_count)
