def main():
    print("Profit Margin Calculator")
    print()
    
    while True:
        profit = get_valid_float("Enter profit amount: $")
        revenue = get_valid_float("Enter revenue amount: $")
        
        try:
            ratio = (profit / revenue) * 100
        except ZeroDivisionError:
            pass
        else:
            print()
            print("Profit Margin Ratio:", ratio, "%")
            break

def get_valid_float(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            pass

main()