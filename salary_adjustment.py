def main():
    print("employee Salary Adjustment System")
    print()

    salary = get_salary()
    
    if salary <= 40000:
        adjustment = 0.15
    elif salary <= 80000:
        adjustment = 0.10
    elif salary <= 120000:
        adjustment = 0.05
    else:
        adjustment = 0.03

    new_salary = salary * (1 + adjustment)
    increase_amount = new_salary - salary

    print()
    print("Current Salary: $", salary)
    print("Adjustment Percentage:", adjustment * 100, "%")
    print("Increase Amount: $", increase_amount)
    print("New Salary: $", new_salary)

def get_salary():
    while True:
        try:
            salary_input = input("Enter current salary ($): ")
            salary = float(salary_input)
            if salary < 0:
                print("Salary cannot be negative.")
            else:
                return salary   
        except ValueError:
            print("Invalid input. Please enter a numeric value for salary.")
    

main()