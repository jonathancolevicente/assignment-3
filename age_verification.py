def main():
    print("Customer Age Verification System")
    print()
        
    try:
        customer_age = get_customer_age()
        
        print()
        if customer_age >= min_age:
            print("Customer is eligible for the promotion.")
        else:
            print("Customer is not eligible for the promotion.")
    except NameError:
        print("Error: Minimum age variable not defined.")

def get_customer_age():
    while True:
        try:
            age = int(input("Enter customer age: "))
            if age > 0:
                return age
            else:
                print("Age must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

main()