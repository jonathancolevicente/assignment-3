Business Python Exceptions

Disclaimer
Note: Almost all coding for these exercises was completed in local files and then uploaded to GitHub in bulk. Due to issues with actively committing changes, the commit history may not reflect the incremental development process.

Python exercises focused on exception handling and input validation for business applications.
Overview
This repository contains five Python programs that demonstrate proper exception handling techniques in real-world business scenarios. Each program uses try-except blocks, input validation loops, and defensive programming practices.
Exercises
Exercise 1: Sales Data Entry System
File: sales_data.py
A retail sales data entry program that prompts for units sold and price per unit, then calculates total revenue.
Features:

Validates integer and float inputs
Reusable get_valid_number() function
Handles ValueError for invalid conversions
Loops until valid data is entered


Exercise 2: Inventory Quantity Checker
File: inventory_checker.py
An inventory management system that checks stock levels against reorder thresholds.
Features:

Validates integer inputs for inventory and threshold
Calculates inventory percentage of threshold
Handles ValueError for non-integer inputs
Handles ZeroDivisionError for zero threshold
Prints reorder alerts when inventory is low


Exercise 3: Customer Age Verification
File: age_verification.py
A marketing tool that verifies customer age eligibility for age-restricted promotions.
Features:

Validates positive integer age input
get_customer_age() function with input validation
Handles ValueError for non-integer inputs
Handles NameError for undefined variables (simulated)
Checks eligibility based on minimum age requirement (18+)


Exercise 4: Profit Margin Calculator
File: profit_margin.py
A finance tool that calculates profit margin ratio as a percentage.
Features:

Validates float inputs for profit and revenue
Uses try-except-else block structure
Handles ValueError for invalid floats
Handles ZeroDivisionError for zero revenue
Silent reprompting with pass statements
Prints ratio in else block only when calculation succeeds


Exercise 5: Employee Salary Adjustment Simulator
File: salary_adjustment.py
An HR tool that simulates employee salary adjustments based on percentage increases.
Features:

Validates float inputs for salary and adjustment percentage
Helper function for input validation
Handles ValueError for non-numeric inputs
Custom validation for negative percentages
Calculates and displays new salary


Key Concepts Demonstrated

Exception Handling: try-except-else blocks
Input Validation: while loops for reprompting
Error Types: ValueError, ZeroDivisionError, NameError
Defensive Programming: pass statements, validation checks
Code Organization: reusable functions, main() structure
Business Logic: revenue calculation, inventory alerts, eligibility checks