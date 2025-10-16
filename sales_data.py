def main():
    print("Sales Data Entry System")
    print()
    
    units_sold = get_valid_number("Enter the number of units sold: ", 'int')
    price_per_unit = get_valid_number("Enter the price per unit ($): ", 'float')
    
    total_revenue = units_sold * price_per_unit
    
    print()
    print("Units Sold:", units_sold)
    print("Price per Unit: $", price_per_unit)
    print("Total Revenue: $", total_revenue)

def get_valid_number(prompt, num_type='int'):
    while True:
        try:
            user_input = input(prompt)
            if num_type == 'int':
                number = int(user_input)
                return number
            else:
                number = float(user_input)
                return number
        except ValueError:
            print("Invalid input. Please enter a valid", num_type)

main()