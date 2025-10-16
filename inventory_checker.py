def main():
    print("Inventory Management System")
    print()
    
    inventory = get_valid_integer("Enter current inventory level: ")
    threshold = get_valid_integer("Enter minimum reorder threshold: ")
    
    try:
        percentage = (inventory / threshold) * 100
        print()
        print("Inventory is at", percentage, "% of threshold")
    except ZeroDivisionError:
        print()
        print("Error: Threshold cannot be zero.")
        return
    
    print()
    if inventory < threshold:
        print("ALERT: Inventory below threshold. Reorder required!")
    else:
        print("Inventory level is adequate.")

def get_valid_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

main()